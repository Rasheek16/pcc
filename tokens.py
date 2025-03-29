patterns = [
    ('char',r'\bchar\b'),
    ('string',r'\bstring\b'),
    ('char_constant',r"""'([^'\\\n]|\\['"?\\abfnrtv])'"""),
    ('string_constant',r'"([^"\\\n]|\\["?\\abfnrtv])*"'),
    ('floating_point_constant',r'(([0-9]*\.[0-9]+|[0-9]+\.?)[Ee][+-]?[0-9]+|[0-9]*\.[0-9]+|[0-9]+\.)[^\w.]'),
    ('double_keyword',r'\bdouble\b'),
     ("Constant", r'([0-9]+)[^\w.]'),
     ("int_keyword", r"int\b"),
     ("void_keyword", r"void\b"),
     ("return_keyword", r"return\b"),
     ('Open_bracket',r'\['),
     ('Close_bracket',r'\]'),
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
     ('if_keyword',r'\bif\b'),
     ('else_keyword',r'\belse\b'),
     ('question_mark',r'\?'),
     ('colon',r':'),
     ('Assignment',r'='),
     ('do',r'\bdo\b'),
     ('while',r'\bwhile\b'),
     ('for',r'\bfor\b'),
     ('break',r'\bbreak\b'),
     ('continue',r'\bcontinue\b'),
     ('comma',r','),
     ('static',r'\bstatic\b'),
     ('extern',r'\bextern\b'),
     ('long_keyword',r'\blong\b'),
     ('signed_keyword',r'\bsigned\b'),
     ('unsigned_keyword',r'\bunsigned\b'),
     ('unsigned_int_constant',r'([0-9]+[uU])[^\w.]'),
     ('long_int_constant',r'([0-9]+[lL])[^\w.]'),
     ('signed_long_constant',r'([0-9]+([lL][uU]|[uU][lL]))[^\w.]'),
    ("Identifier",r"[a-zA-Z_]\w*\b"),
    ('Ampersand',r'&'),
     
]


