# Linguagem

# EBNF
```c
PROGRAM = { STATEMENT } ;
BLOCK = "{", { STATEMENT }, "}" ;
STATEMENT = ( λ | ASSIGNMENT | PRINT | IF | FOR | WHILE | VARIABLE | CREATION | CREATEADVANTAGE | CHECKITEMS ), "\n" ;
ASSIGNMENT = IDENTIFIER, "=", BOOLEXPRESSION ;
PRINT = "print", "(", BOOLEXPRESSION, ")" ;
CHECKITEMS = "checkIt", "(", ")" ;
IF = "if", BOOLEXPRESSION, BLOCK, ( λ | "else", BLOCK ) ;
FOR = "for", ASSIGNMENT, ";", BOOLEXPRESSION, ";", ASSIGNMENT, BLOCK ;
WHILE = "while", BOOLEXPRESSION, BLOCK ;
VARIABLE = TYPE, IDENTIFIER, ( λ | "=", BOOLEXPRESSION ) ;
CREATION = "character", IDENTIFIER, "(", "type", IDENTIFIER, ";", "health", IDENTIFIER, ";", "attack", IDENTIFIER, ")" ;
CREATEADVANTAGE = "advantage", "(", IDENTIFIER, ",", IDENTIFIER, ")" ;
BOOLEXPRESSION = BOOLTERM, { ( "or" ), BOOLTERM } ;
BOOLTERM = RELATIONALEXPRESSION, { ( "and" ), RELATIONALEXPRESSION } ;
RELATIONALEXPRESSION = EXPRESSION, { ( "==" | ">" | "<" ), EXPRESSION } ;
EXPRESSION = TERM, { ( "+" | "-" | "." ), TERM } ;
TERM = FACTOR, { ( "*" | "/" ), FACTOR } ;
FACTOR = ( ( "+" | "-" | "not" ), FACTOR ) | NUMBER | "(", BOOLEXPRESSION, ")" | IDENTIFIER | FUNCTIONS ;
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
TYPE = ( "type" | "int" | "character" | "items" ) ;
```