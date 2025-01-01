patterns = [
    ("Identifier",r"[a-zA-Z_]\w*\b"),
     ("Constant", r"[0-9]+\b"),
     ("int_keyword", r"int\b"),
     ("void_keyword", r"void\b"),
     ("return_keyword", r"return\b"),
     ("Open_parenthesis", r"\("),
     ("Close_parenthesis", r"\)"),
     ("Open_brace", r"{"),
     ("Close_brace", r"}"),
     ("Semicolon", r";"),
     ("Complement",r'~'),
     ("Decrement",r'--'),
     ("Negation",r'-'),
     ("Multiplication",r"\*"),
     ("Addition",r'\+'),
     ("Division",r'/'),
     ("Remainder",r'%'),
     ("And",r'\&\&'),
     ("LessOrEqual",r'<='),
     ("GreaterOrEqual",r'>='),   
     ("Or",r'\|\|'),
     ("Equal",r'\=\='),
     ("NotEqual",r'\!\='),
     ("Not",r'!'),
     ("LessThan",r'\<'),
     ("GreaterThan",r'\>'),
     ('if_keyword',r'if'),
     ('else_keyword',r'else'),
     ('question_mark',r'\?'),
     ('colon',r':'),
     ('Assignment',r'=')
     
]
