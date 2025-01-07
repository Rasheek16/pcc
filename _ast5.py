from typing import List, Optional, Union
from enum import Enum


# --------------------------
# Enum Definitions for Operators
# --------------------------

class UnaryOperator():
    """
    Enumeration of supported unary operators.
    
    Attributes:
        COMPLEMENT: Represents the bitwise complement operator (~).
        NEGATE: Represents the arithmetic negation operator (-).
        NOT: Represents the logical NOT operator (!).
    """
    COMPLEMENT = "Complement"  # e.g., ~x
    NEGATE = "Negate"          # e.g., -x
    NOT = "Not"                # e.g., !x


class BinaryOperator():
    """
    Enumeration of supported binary operators.
    
    Attributes:
        ADD: Represents the addition operator (+).
        SUBTRACT: Represents the subtraction operator (-).
        MULTIPLY: Represents the multiplication operator (*).
        DIVIDE: Represents the division operator (/).
        REMAINDER: Represents the modulus operator (%).
        AND: Represents the logical AND operator (&&).
        OR: Represents the logical OR operator (||).
        EQUAL: Represents the equality operator (==).
        NOT_EQUAL: Represents the inequality operator (!=).
        LESS_THAN: Represents the less-than operator (<).
        LESS_OR_EQUAL: Represents the less-than-or-equal-to operator (<=).
        GREATER_THAN: Represents the greater-than operator (>).
        GREATER_OR_EQUAL: Represents the greater-than-or-equal-to operator (>=).
    """
    ADD = "Add"                    # e.g., a + b
    SUBTRACT = "Subtract"          # e.g., a - b
    MULTIPLY = "Multiply"          # e.g., a * b
    DIVIDE = "Divide"              # e.g., a / b
    REMAINDER = "Remainder"        # e.g., a % b
    AND = "And"                    # e.g., a && b
    OR = "Or"                      # e.g., a || b
    EQUAL = "Equal"                # e.g., a == b
    NOT_EQUAL = "NotEqual"         # e.g., a != b
    LESS_THAN = "LessThan"         # e.g., a < b
    LESS_OR_EQUAL = "LessOrEqual"  # e.g., a <= b
    GREATER_THAN = "GreaterThan"   # e.g., a > b
    GREATER_OR_EQUAL = "GreaterOrEqual"  # e.g., a >= b
    ASSIGNMENT = 'Assignment'


# --------------------------
# Identifier Class
# --------------------------

class Identifier:
    """
    Represents an identifier, such as function names or variable names.
    
    Attributes:
        name (str): The name of the identifier.
    """
    def __init__(self, name: str):
        """
        Initializes an Identifier instance.
        
        Args:
            name (str): The name of the identifier.
        """
        self.name = name

    def __repr__(self) :
        """
        Returns a string representation of the Identifier.
        
        Returns:
            str: The string representation.
        """
        return f"Identifier(name={self.name})"


    
    

# --------------------------
# Expression Classes
# --------------------------

class Exp:
    """
    Base class for all exp in the AST.
    """
    pass


class Constant(Exp):
    """
    Represents an integer constant in the AST.
    
    Attributes:
        value (int): The integer value of the constant.
    """
    def __init__(self, value: int):
        """
        Initializes a Constant instance.
        
        Args:
            value (int): The integer value.
        """
        self.value = value  # integer value

    def __repr__(self) :
        """
        Returns a string representation of the Constant.
        
        Returns:
            str: The string representation.
        """
        return f"Constant(value={self.value})"


class Var(Exp):
    """
    Represents a variable access in the AST.
    
    Attributes:
        identifier (Identifier): The identifier of the variable.
    """
    def __init__(self, identifier: Identifier):
        """
        Initializes a Var instance.
        
        Args:
            identifier (Identifier): The variable's identifier.
        
        Raises:
            ValueError: If the identifier is not an instance of Identifier.
        """
        # if not isinstance(identifier, Identifier):
        #     raise ValueError("Var expects an Identifier instance.")
        self.identifier = identifier  # Corrected attribute name

    def __repr__(self) :
        """
        Returns a string representation of the Var.
        
        Returns:
            str: The string representation.
        """
        return f"Var(identifier={self.identifier})"


class Unary(Exp):
    """
    Represents a unary operation in the AST.
    
    Attributes:
        operator (UnaryOperator): The unary operator.
        expr (Exp): The operand expression.
    """
    def __init__(self, operator: UnaryOperator, expr: Exp):
        """
        Initializes a Unary instance.
        
        Args:
            operator (UnaryOperator): The unary operator.
            expr (Exp): The operand expression.
        
        Raises:
            ValueError: If the operator is not a valid UnaryOperator.
        """
        
        self.operator = operator
        self.expr = expr

    def __repr__(self) :
        """
        Returns a string representation of the Unary operation.
        
        Returns:
            str: The string representation.
        """
        return f"Unary(operator={self.operator}, expr={self.expr})"


class Binary(Exp):
    """
    Represents a binary operation in the AST.
    
    Attributes:
        operator (BinaryOperator): The binary operator.
        left (Exp): The left operand expression.
        right (Exp): The right operand expression.
    """
    def __init__(self, operator: BinaryOperator, left: Exp, right: Exp):
        """
        Initializes a Binary instance.
        
        Args:
            operator (BinaryOperator): The binary operator.
            left (Exp): The left operand.
            right (Exp): The right operand.
        
        Raises:
            ValueError: If the operator is not a valid BinaryOperator.
        """
        # if not isinstance(operator, BinaryOperator):
        #     raise ValueError(f"Invalid binary operator: {operator}")
        # if not isinstance(left, Exp) or not isinstance(right, Exp):
        #     raise ValueError("Binary operation requires Exp instances as operands.")
        self.operator = operator
        self.left = left
        self.right = right

    def __repr__(self) :
        """
        Returns a string representation of the Binary operation.
        
        Returns:
            str: The string representation.
        """
        return (f"Binary(operator={self.operator}, "
                f"left={self.left}, right={self.right})")


class Assignment(Exp):
    """
    Represents an assignment operation in the AST.
    
    Attributes:
        left (Exp): The left-hand side expression.
        right (Exp): The right-hand side expression.
    """
    def __init__(self, left: Exp, right: Exp):
        """
        Initializes an Assignment instance.
        
        Args:
            left (Exp): The variable being assigned to.
            right (Exp): The expression being assigned.
        
        Raises:
            ValueError: If either left or right is not an Exp instance.
        """
        # if not isinstance(left, Exp) or not isinstance(right, Exp):
        #     raise ValueError("Both left and right must be Exp instances.")
        self.left = left
        self.right = right

    def __repr__(self) :
        """
        Returns a string representation of the Assignment.
        
        Returns:
            str: The string representation.
        """
        return f"Assignment(left={self.left}, right={self.right})"

class FunctionCall(Exp):
    def __init__(self,identifier:Identifier,args:List[Exp]):
        self.identifier = identifier
        self.args = args
        
    def __repr__(self):
        return f'\nFunctionCall(identifier = {self.identifier},args = {self.args})'
# --------------------------
# Declaration Class
# --------------------------

class Declaration:
    
    def __init__(self, *args, **kwargs):
        # super(CLASS_NAME, self).__init__(*args, **kwargs)
        pass 
    
    # """
    # Represents a variable declaration in the AST.
    
    # Attributes:
    #     name (Identifier): The name of the variable being declared.
    #     init (Optional[Exp]): The optional initializer expression.
    # """
    # def __init__(self, name: Identifier, init: Optional[Exp] = None):
    #     """
    #     Initializes a Declaration instance.
        
    #     Args:
    #         name (Identifier): The variable's identifier.
    #         init (Optional[Exp]): The initializer expression, if any.
        
    #     Raises:
    #         ValueError: If name is not an Identifier instance or init is not an Exp instance.
    #     """
    #     # if not isinstance(name, Identifier):
    #     #     raise ValueError("Declaration name must be an Identifier instance.")
    #     # if init is not None and not isinstance(init, Exp):
    #     #     raise ValueError("Initializer must be an Exp instance or None.")
    #     self.name = name
    #     self.init = init

    # def __repr__(self) -> str:
        # """
        # Returns a string representation of the Declaration.
        
        # Returns:
        #     str: The string representation.
        # """
        # if self.init:
        #     return f"Declaration(name={self.name}, init={self.init})"
        # else:
            # return f"Declaration(name={self.name}, init=None)"

class Block:
    def __init__(self, block_items: List):
        self.block_items = block_items

    def __iter__(self):
        return iter(self.block_items)

    def __repr__(self):
        items_repr = ",\n        ".join(repr(item) for item in self.block_items)
        return f"Block([\n        {items_repr}\n    ])"
    

class Parameter():
    def __init__(self, _type,name:Optional[Identifier]):
        self._type=_type
        self.name = name 
    def __repr__(self):
        return f'Parameter(type={self._type},name = {self.name})'

class FunctionDeclaration():
    def __init__(self,_name:Identifier,params:List[Parameter],body=Optional[Block]):    
        self._name=_name
        self.params=params
        self.body=body
    
class VariableDeclaration():
    name:Identifier
    init:Optional[Exp]
    
class FunDecl(Declaration):
    def __init__(self,name:Identifier,params:List[Parameter],body:Optional[Block]=None):    
            self.name=name
            self.params=params
            self.body=body
        
    def __repr__(self):
        return f'FunDecl(name={self.name},params={self.params},body={self.body})'


class VarDecl(Declaration):
    
    def __init__(self,name:Identifier,init:Optional[Exp]):
        self.name=name
        self.init=init
        
    def __repr__(self):
        return f'VarDecl(name={self.name},init={self.init})'

# --------------------------
# Statement Classes
# --------------------------

class Statement:
    """
    Base class for all statements in the AST.
    """
    pass


class Return(Statement):
    """
    Represents a return statement in the AST.
    
    Attributes:
        exp (Exp): The expression to be returned.
    """
    def __init__(self, exp: Exp):
        """
        Initializes a Return instance.
        
        Args:
            exp (Exp): The expression to return.
        
        Raises:
            ValueError: If exp is not an Exp instance.
        # """
        # if not isinstance(exp, Exp):
        #     raise ValueError("Return statement requires an Exp instance.")
        self.exp = exp

    def __repr__(self) :
        """
        Returns a string representation of the Return statement.
        
        Returns:
            str: The string representation.
        """
        return f"Return(exp={self.exp})"


class Expression(Statement):
    """
    Represents an expression statement in the AST.
    
    Attributes:
        exp (Exp): The expression being evaluated.
    """
    def __init__(self, exp: Exp):
        """
        Initializes an Expression statement instance.
        
        Args:
            exp (Exp): The expression to evaluate.
        
        Raises:
            ValueError: If exp is not an Exp instance.
        """
        # if not isinstance(exp, Exp):
        #     raise ValueError("Expression statement requires an Exp instance.")
        self.exp = exp

    def __repr__(self) :
        """
        Returns a string representation of the Expression statement.
        
        Returns:
            str: The string representation.
        """
        return f"Expression(exp={self.exp})"

class If(Statement):

    def __init__(self, exp: Exp,then, _else=None):
   
        self.exp = exp
        self.then = then 
        self._else = _else

    def __repr__(self) :
        """
        Returns a string representation of the Expression statement.
        
        Returns:
            str: The string representation.
        """
        return f"If(\nexp={self.exp},Then = {self.then}, else = {self._else}\n)"


class Conditional(Statement):

    def __init__(self, condition: Exp, exp2,exp3):
   
        self.condition = condition
        self.exp2 = exp2
        self.exp3 = exp3

    def __repr__(self) :
        """
        Returns a string representation of the Expression statement.
        
        Returns:
            str: The string representation.
        """
        return f"Condition(condition={self.condition},exp2 = {self.exp2}, exp3 = {self.exp3})"


class Null(Statement):
    """
    Represents a null statement (no operation) in the AST.
    """
    def __init__(self):
        """
        Initializes a Null statement instance.
        """
        pass

    def __repr__(self) :
        """
        Returns a string representation of the Null statement.
        
        Returns:
            str: The string representation.
        """
        return "Null()"


    

    
class Argument():
    def __init__(self, name:Exp):
      
        self.name = name 
    def __repr__(self):
        return f'Argument(name = {self.name})'
     

# --------------------------
# Block Item Classes
# --------------------------

class BlockItem:
    """
    Base class for block items in the function body.
    """
    pass


class S(BlockItem):
    """
    Represents a statement block item.
    
    Attributes:
        statement (Statement): The statement contained in the block.
    """
    def __init__(self, statement: Statement):
        """
        Initializes an S (Statement) block item.
        
        Args:
            statement (Statement): The statement to include in the block.
        
        Raises:
            ValueError: If statement is not a Statement instance.
        """
        # if not isinstance(statement, Statement):
        #     raise ValueError("S expects a Statement instance.")
        self.statement = statement

    def __repr__(self) :
        """
        Returns a string representation of the S block item.
        
        Returns:
            str: The string representation.
        """
        return f"S(statement={self.statement})"


class D(BlockItem):
    """
    Represents a declaration block item.
    
    Attributes:
        declaration (Declaration): The declaration contained in the block.
    """
    def __init__(self, declaration: Declaration):
        """
        Initializes a D (Declaration) block item.
        
        Args:
            declaration (Declaration): The declaration to include in the block.
        
        Raises:
            ValueError: If declaration is not a Declaration instance.
        """
        # if not isinstance(declaration, Declaration):
        #     raise ValueError("D expects a Declaration instance.")
        self.declaration = declaration

    def __repr__(self) :
        """
        Returns a string representation of the D block item.
        
        Returns:
            str: The string representation.
        """
        return f"D(declaration={self.declaration})"

class Block:
    def __init__(self, block_items: List):
        self.block_items = block_items

    def __iter__(self):
        return iter(self.block_items)

    def __repr__(self):
        items_repr = ",\n        ".join(repr(item) for item in self.block_items)
        return f"Block([\n        {items_repr}\n    ])"
    
    
class Compound(Statement):
    def __init__(self, block:Block):
        self.block = block 
        
    def __repr__(self):
        return f'Compound(block={self.block})'

class Break(Statement):
    def __init__(self,label:Identifier =None):
        self.label = label 
    
    def __repr__(self):
        return f'\nBreak(identifier={self.label}\n)'
    

class Continue(Statement):
    def __init__(self,label:Identifier=None):
        self.label = label 
    
    def __repr__(self):
        return f'Continue(identifier={self.label})'
    

class While(Statement):
    def __init__(self,_condition:Exp,body:Statement,label:Identifier=None):
        self._condition =_condition 
        self.body = body 
        self.label = label 

    def __repr__(self):
        return f'While(condition={self._condition},body={self.body},identifier={self.label})'
        
        
class DoWhile(Statement):
    def __init__(self,body:Statement,_condition:Exp,label:Identifier=None):
        self._condition =_condition 
        self.body = body 
        self.label = label 

    def __repr__(self):
        return f'DoWhile(body={self.body},condition={self._condition},identifier={self.label})'


class ForInit():
    def __init__(self):
        pass 
        # super(CLASS_NAME, self).__init__(*args, **kwargs)

class InitDecl(ForInit):
    def __init__(self,declaration:D):
        self.declaration = declaration
 
       # super(CLASS_NAME, self).__init__(*args, **kwarg)
    def __repr__(self):
        return f'InitDecl(declaration={self.declaration})'

class InitExp(ForInit):
    def __init__(self,exp:Expression=None):
        self.exp = exp
 
       # super(CLASS_NAME, self).__init__(*args, **kwarg)
    def __repr__(self):
        return f'InitExp(exp={self.exp})'
class For(Statement):
    def __init__(self,init: ForInit,condition:Exp=None , post:Exp = None, body:Statement=None,label:Identifier=None ):
        self.init =init
        self.condition = condition
        self.body= body
        self.post=post
        self.label = label 

    def __repr__(self):
        return f'\nFor(init={self.init},condition={self.condition},body={self.body},identifier={self.label}.post={self.post}\n)'



# --------------------------
# Function and Program Classes
# --------------------------

class Function:
    """
    Represents a function definition in the AST.
    
    Attributes:
        name (Identifier): The name of the function.
        body (List[BlockItem]): The list of block items comprising the function's body.
    """
    def __init__(self, name: Identifier, body:  Block):
        """
        Initializes a Function instance.
        
        Args:
            name (Identifier): The function's identifier.
            body (List[BlockItem]): The function's body as a list of block items.
        
        Raises:
            ValueError: If name is not an Identifier or if any item in body is not a BlockItem.
        """
        # if not isinstance(name, Identifier):
        #     raise ValueError("Function name must be an Identifier instance.")
        # if not all(isinstance(item, BlockItem) for item in body):
        #     raise ValueError("All items in body must be BlockItem instances.")
        self.name = name
        self.body = body

    def __repr__(self) :
        """
        Returns a string representation of the Function.
        
        Returns:
            str: The string representation.
        """
        # Join the representations of all block items with indentation for readability
        body_repr = ',\n        '.join(repr(item) for item in self.body)
        return (f"\nFunction(name={self.name}, body=[\n        {body_repr}\n    ]\n)")


class Program:
    """
    Represents the entire program in the AST.
    
    Attributes:
        function_definition (Function): The main function definition of the program.
    """
    def __init__(self, function_definition:List[FunDecl]):
        """
        Initializes a Program instance.
        
        Args:
            function_definition (Function): The main function of the program.
        
        Raises:
            ValueError: If function_definition is not a Function instance.
        """
        # if not isinstance(function_definition, Function):
        #     raise ValueError("Program expects a Function instance.")
        self.function_definition = function_definition

    def __repr__(self) -> str:
        """
        Returns a string representation of the Program.
        
        Returns:
            str: The string representation.
        """
        return f"Program(\n  functions={self.function_definition}\n)"



class Parameter():
    def __init__(self, _type,name:Optional[Identifier]=None):
        self._type=_type
        self.name = name 
    def __repr__(self):
        return f'Parameter(type={self._type},name = {self.name})'
    
class Argument():
    def __init__(self, name:Exp):
      
        self.name = name 
    def __repr__(self):
        return f'Argument(name = {self.name})'
     
    
    
class Int():
    
    def __init__(self, *args, **kwargs):
        # super(CLASS_NAME, self).__init__(*args, **kwargs)
        pass
    
    def __repr__(self):
        return f'Int()'


class FunType():
    
    def __init__(self, param_count:int):
        self.param_count = param_count
        
    def __repr__(self):
        return f'FunType(param_count={self.param_count})'
    