# Linguagem

# EBNF
```c
PROGRAM = { DECLARATION } ;
DECLARATION = "func", IDENTIFIER, "(", ( λ | IDENTIFIER, TYPE, { ",", IDENTIFIER, TYPE } ), ")", TYPE, BLOCK, "\n" ;
BLOCK = "{", { STATEMENT }, "}" ;
STATEMENT = ( λ | ASSIGNMENT | PRINT | IF | FOR | WHILE | VARIABLE | RETURN | CREATION | CREATEADVANTAGE | CHECKITEMS ), "\n" ;
ASSIGNMENT = IDENTIFIER, ( "=", BOOLEXPRESSION | ARGS ) ;
ARGS = "(", ( λ | BOOLEXPRESSION, { ",", BOOLEXPRESSION } ), ")" ;
PRINT = "print", "(", BOOLEXPRESSION, ")" ;
CHECKITEMS = "checkIt", "(", ")" ;
IF = "if", BOOLEXPRESSION, BLOCK, ( λ | "else", BLOCK ) ;
FOR = "for", ASSIGNMENT, ";", BOOLEXPRESSION, ";", ASSIGNMENT, BLOCK ;
WHILE = "while", BOOLEXPRESSION, BLOCK ;
VARIABLE = TYPE, IDENTIFIER, ( λ | "=", BOOLEXPRESSION ) ;
RETURN = "return", BOOLEXPRESSION ;
CREATION = "character", IDENTIFIER, "(", "type", IDENTIFIER, ";", "health", IDENTIFIER, ";", "attack", IDENTIFIER, ")" ;
CREATEADVANTAGE = "advantage", "(", IDENTIFIER, ",", IDENTIFIER, ")" ;
BOOLEXPRESSION = BOOLTERM, { ( "or" ), BOOLTERM } ;
BOOLTERM = RELATIONALEXPRESSION, { ( "and" ), RELATIONALEXPRESSION } ;
RELATIONALEXPRESSION = EXPRESSION, { ( "==" | ">" | "<" ), EXPRESSION } ;
EXPRESSION = TERM, { ( "+" | "-" | "." ), TERM } ;
TERM = FACTOR, { ( "*" | "/" ), FACTOR } ;
FACTOR = ( ( "+" | "-" | "not" ), FACTOR ) | NUMBER | "(", BOOLEXPRESSION, ")" | IDENTIFIER, ( λ | ARGS ) | STRING | FUNCTIONS ;
FUNCTIONS = SCANTEXT | SCANNUMBER | RANDOM | CHECKADVANTAGE | CHECKSTATUS ;
SCANTEXT = "scanText", "(", ")" ;
SCANNUMBER = "scanNumber", "(", ")" ;
RANDOM = "random", "(", NUMBER, ")" ;
CHECKADVANTAGE = "checkAdv", "(", IDENTIFIER, ",", IDENTIFIER, ")" ;
CHECKSTATUS = "checkSt", "(", IDENTIFIER, ",", IDENTIFIER, ")" ;
IDENTIFIER = LETTER, { LETTER } ;
NUMBER = DIGIT, { DIGIT } ;
LETTER = ( a | ... | z | A | ... | Z ) ;
DIGIT = ( 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0 ) ;
STRING = ( '"' , { CHAR } , '"' | "'" , { CHAR } , "'" ) ;
CHAR = ( LETTER | DIGIT | "_" | "+" | "-" | "*" | "/" | " " | "!" | "@" | "#" | "$" | "%" | "^" | "&" | "(" | ")" | "[" | "]" | "{" | "}" | "'" | "\"" | ":" | ";" | "," | "." | "?" | "=" ) ;
TYPE = ( "type" | "int" | "character" | "items" ) ;
```