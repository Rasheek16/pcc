from tacky import *
from assembly_ast import Mov, Ret, Imm, Registers, AssemblyFunction, AssemblyProgram, Reg, Unary, Pseudo , UnaryOperator ,Stack ,AllocateStack,Cqd,Idiv,Binary,BinaryOperator
import sys
from typing import Union, List ,Dict

def convert_to_assembly_ast(tacky_ast) -> AssemblyProgram:
    """
    Converts a Tacky AST into an AssemblyProgram AST.
    
    Args:
        tacky_ast: The root of the Tacky AST to be converted.
    
    Returns:
        An AssemblyProgram instance representing the equivalent assembly code.
    """
    # Handle the top-level Program node
    
    if isinstance(tacky_ast, TackyProgram):
        # Recursively convert the function_definition part of the TackyProgram
        assembly_function = convert_to_assembly_ast(tacky_ast.function_definition)
        return AssemblyProgram(
            function_definition=assembly_function
        )
    
    # Handle Function node
    elif isinstance(tacky_ast, TackyFunction):
        instructions = []
        # Iterate over each instruction in the TackyFunction
        # print(instructions)
        for instr in tacky_ast.body[0]:
            # Convert each instruction and collect them
            converted_instrs = convert_to_assembly_ast(instr)
            if isinstance(converted_instrs, list):
                # If conversion returns a list of instructions, extend the list
                instructions.extend(converted_instrs)
            else:
                # Otherwise, append the single instruction
                instructions.append(converted_instrs)
        # Create an AssemblyFunction with the converted instructions
        return AssemblyFunction(
            name=tacky_ast.name,  # Assuming tacky_ast.name is an Identifier
            instructions=instructions
        )
    
    # Handle Return instruction
    elif isinstance(tacky_ast, TackyReturn):
        # Convert a Return by moving the value into AX and issuing a Ret
        return [
            Mov(src=convert_to_assembly_ast(tacky_ast.val), dest=Reg(Registers.AX)),
            Ret()
        ]
    
    # Handle Unary instruction
    elif isinstance(tacky_ast, TackyUnary):        
        # Convert a Unary operation by moving src to dst and applying the operator
        return [
            Mov(src=convert_to_assembly_ast(tacky_ast.src), dest=convert_to_assembly_ast(tacky_ast.dst)),
            Unary(operator=convert_operator(tacky_ast.operator), operand=convert_to_assembly_ast(tacky_ast.dst))
        ]
        
    # Check if the current AST node is a TackyBinary operation
    elif isinstance(tacky_ast, TackyBinary):
        
        # Handle integer division operations
        if tacky_ast.operator == TackyBinaryOperator.DIVIDE:
            """
            Generate assembly instructions for integer division.
            
            Assembly Operations:
                1. Move the dividend (src1) into the AX register.
                2. Execute the CDQ instruction to sign-extend AX into DX:AX.
                3. Perform the IDIV operation using the divisor (src2).
                4. Move the quotient from AX to the destination (dst).
            
            This sequence follows the x86 assembly convention for signed integer division.
            """
            return [
                # Move the dividend to the AX register
                Mov(src=convert_to_assembly_ast(tacky_ast.src1), dest=Reg(Registers.AX)),
                
                # Convert Doubleword to Quadword: Sign-extend AX into DX:AX
                Cqd(),
                
                # Perform signed integer division: AX / src2
                Idiv(operand=convert_to_assembly_ast(tacky_ast.src2)),
                
                # Move the quotient from AX to the destination variable
                Mov(src=Reg(Registers.AX), dest=convert_to_assembly_ast(tacky_ast.dst))
            ]
        
        # Handle remainder operations resulting from integer division
        elif tacky_ast.operator == TackyBinaryOperator.REMAINDER:
            """
            Generate assembly instructions for computing the remainder after integer division.
            
            Assembly Operations:
                1. Move the dividend (src1) into the AX register.
                2. Execute the CDQ instruction to sign-extend AX into DX:AX.
                3. Perform the IDIV operation using the divisor (src2).
                4. Move the remainder from DX to the destination (dst).
            
            This sequence adheres to the x86 assembly convention where the remainder is stored in the DX register after division.
            """
            return [
                # Move the dividend to the AX register
                Mov(src=convert_to_assembly_ast(tacky_ast.src1), dest=Reg(Registers.AX)),
                
                # Convert Doubleword to Quadword: Sign-extend AX into DX:AX
                Cqd(),
                
                # Perform signed integer division: AX / src2
                Idiv(operand=convert_to_assembly_ast(tacky_ast.src2)),
                
                # Move the remainder from DX to the destination variable
                Mov(src=Reg(Registers.DX), dest=convert_to_assembly_ast(tacky_ast.dst))
            ]
        
        # Handle addition, subtraction, and multiplication operations
        elif tacky_ast.operator in (
            TackyBinaryOperator.ADD,
            TackyBinaryOperator.SUBTRACT,
            TackyBinaryOperator.MULTIPLY
        ):
            """
            Generate assembly instructions for addition, subtraction, and multiplication.
            
            Assembly Operations:
                1. Move the first operand (src1) directly into the destination register.
                2. Perform the binary operation (ADD, SUBTRACT, MULTIPLY) between the second operand (src2) and the destination register.
            
            This approach optimizes instruction generation by utilizing the destination register to store intermediate results, reducing the need for additional temporary storage.
            """
            return [
                # Move the first operand directly into the destination register
                Mov(src=convert_to_assembly_ast(tacky_ast.src1), dest=convert_to_assembly_ast(tacky_ast.dst)),
                
                # Perform the binary operation with the second operand and store the result in the destination register
                Binary(
                    operator=tacky_ast.operator,
                    src1=convert_to_assembly_ast(tacky_ast.src2),
                    src2=convert_to_assembly_ast(tacky_ast.dst)
                )
            ]
    
        # Handle unsupported binary operators by raising an error
        else:
            """
            Error Handling:
                If the binary operator is not among the supported ones (DIVIDE, REMAINDER, ADD, SUBTRACT, MULTIPLY),
                the compiler raises a TypeError to indicate that the expression type is unsupported.
            """
            raise TypeError(f"Unsupported binary operator: {tacky_ast.operator}")


    
    # Handle Constant operand
    elif isinstance(tacky_ast, TackyConstant):
        # Convert a constant value into an Imm operand
        return Imm(tacky_ast.value)
    
    # Handle Variable operand
    elif isinstance(tacky_ast, TackyVar):
        # Convert a variable into a Pseudo operand
        # print(tacky_ast)
        return Pseudo(tacky_ast.identifier)
    
    else:
        # Print error message for unsupported AST nodes and exit
        print(f"Unsupported AST node: {type(tacky_ast).__name__}", file=sys.stderr)
        sys.exit(1)


def convert_operator(op: str) -> str:
    """
    Converts a Tacky unary or binary operator to its Assembly equivalent.
    
    Args:
        op (str): The operator from the Tacky AST. 
                  - For unary operators: 'Complement' or 'Negate'/'Negation'
                  - For binary operators: 'Add', 'Subtract', 'Multiply'
    
    Returns:
        str: A string representing the corresponding Assembly operator, as defined in the 
             UnaryOperator or BinaryOperator enums.
    
    Raises:
        ValueError: If the operator is unrecognized or not supported.
    """
    # Handle unary bitwise NOT operator
    if op == 'Complement':
        return UnaryOperator.NOT  # Corresponds to the bitwise NOT operation, e.g., '~x'
    
    # Handle unary arithmetic negation operators
    elif op in ('Negate', 'Negation'):
        return UnaryOperator.NEG  # Corresponds to the arithmetic negation operation, e.g., '-x'
    
    # Handle binary addition operator
    elif op == 'Add':
        return BinaryOperator.ADD  # Corresponds to the addition operation, e.g., 'x + y'
    
    # Handle binary subtraction operator
    elif op == 'Subtract':
        return BinaryOperator.SUBTRACT  # Corresponds to the subtraction operation, e.g., 'x - y'
    
    # Handle binary multiplication operator
    elif op == 'Multiply':
        return BinaryOperator.MULTIPLY  # Corresponds to the multiplication operation, e.g., 'x * y'
    
    # If the operator does not match any known unary or binary operators, raise an error
    else:
        # Raises a ValueError with a descriptive message indicating the unsupported operator
        raise ValueError(f"Unknown operator: {op}")





def replace_pseudoregisters(assembly_program: AssemblyProgram) -> int:
    """
    Replaces all Pseudo operands in the Assembly AST with Stack operands.
    
    Args:
        assembly_program (AssemblyProgram): The AssemblyProgram AST to process.
        
    Returns:
        int: The total number of bytes to allocate on the stack.
    """
    pseudo_map: Dict[str, int] = {}
    current_offset: int = -4  # Start at -4(%rbp)
    
    # Access the single AssemblyFunction within the AssemblyProgram
    assembly_function: AssemblyFunction = assembly_program.function_definition
    
    for instr in assembly_function.instructions:
        if isinstance(instr, Mov):
            # Replace src if it's a Pseudo
            if isinstance(instr.src, Pseudo):
                pseudo_name = instr.src.identifier
                if pseudo_name not in pseudo_map:
                    pseudo_map[pseudo_name] = current_offset
                    current_offset -= 4
                instr.src = Stack(pseudo_map[pseudo_name])
            
            # Replace dest if it's a Pseudo
            if isinstance(instr.dest, Pseudo):
                pseudo_name = instr.dest.identifier
                if pseudo_name not in pseudo_map:
                    pseudo_map[pseudo_name] = current_offset
                    current_offset -= 4
                instr.dest = Stack(pseudo_map[pseudo_name])
        
        elif isinstance(instr, Unary):
            # Replace operand if it's a Pseudo
            if isinstance(instr.operand, Pseudo):
                pseudo_name = instr.operand.identifier
                if pseudo_name not in pseudo_map:
                    pseudo_map[pseudo_name] = current_offset
                    current_offset -= 4
                instr.operand = Stack(pseudo_map[pseudo_name])
        
        # AllocateStack and Ret do not contain Pseudos to replace
        elif isinstance(instr, AllocateStack):
            # Optionally, handle AllocateStack if needed
            pass
        elif isinstance(instr, Ret):
            # No operands to replace in Ret
            pass
        else:
            print(f"Unsupported instruction type: {type(instr)}")
            sys.exit(1)
    
    # Calculate total stack allocation
    # Since current_offset starts at -4 and decrements by 4 for each new Pseudo,
    # the total allocation is abs(current_offset + 4)
    total_stack_allocation = abs(current_offset + 4)
    
    return total_stack_allocation


def fix_up_instructions(assembly_program: AssemblyProgram, stack_allocation: int) -> None:
    """
    Performs two fixes on the Assembly AST:
    1. Inserts an AllocateStack instruction at the beginning of each function's instruction list.
    2. Rewrites invalid Mov instructions where both src and dest are Stack operands.
    
    Args:
        assembly_program (AssemblyProgram): The AssemblyProgram AST to process.
        stack_allocation (int): The total stack space required based on allocated temporaries.
    
    Returns:
        None. The function modifies the assembly_program in place.
    """
    # Access the single AssemblyFunction within the AssemblyProgram
    assembly_function: AssemblyFunction = assembly_program.function_definition
    
    # 1. Insert AllocateStack at the beginning of the instruction list
    allocate_instr = AllocateStack(value=stack_allocation)
    assembly_function.instructions.insert(0, allocate_instr)
    # Debug Statement
    print(f"Inserted AllocateStack({allocate_instr.value}) at the beginning of function '{assembly_function.name}'.")
    
    # 2. Traverse the instruction list to find and fix invalid Mov instructions
    new_instructions: List = []
    
    for instr in assembly_function.instructions:
        if isinstance(instr, Mov):
            # Check if both src and dest are Stack operands
            if isinstance(instr.src, Stack) and isinstance(instr.dest, Stack):
                # Invalid Mov: both src and dest are Stack operands
                
                # Create a Mov from src Stack to R10D
                mov_to_reg = Mov(src=instr.src, dest=Reg(Registers.R10))
                # Create a Mov from R10D to dest Stack
                mov_to_dest = Mov(src=Reg(Registers.R10), dest=instr.dest)
                
                # Append the two new Mov instructions instead of the invalid one
                new_instructions.extend([mov_to_reg, mov_to_dest])
                
                # Debug Statement
                print(f"Rewrote invalid Mov instruction from {instr.src} to {instr.dest} using {Registers.R10}.")
            else:
                # Valid Mov instruction; keep as-is
                new_instructions.append(instr)
        else:
            # Other instructions; keep as-is
            new_instructions.append(instr)
    
    # Update the function's instruction list with the new instructions
    assembly_function.instructions = new_instructions
    # Debug Statement
    print(f"Completed fixing instructions for function '{assembly_function.name}'.")
