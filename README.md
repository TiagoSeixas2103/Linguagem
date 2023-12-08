# Status dos testes
![git status](http://3.129.230.99/svg/TiagoSeixas2103/LogicaComputacional/)

# Diagrama Sintatico
![alt text](img/diagramaSintatico.png)

# EBNF
```c

PROGRAM = { STATEMENT };
DECLARATION = "def", ( TYPE | TYPEVOID ), IDENTIFIER, "(", ( λ | TYPE, IDENTIFIER, { ",", TYPE, IDENTIFIER } ), ")", ":", BLOCK, "\n" ;
BLOCK = "\n", { STATEMENT }, "end" ;
STATEMENT = ( λ | ASSIGNMENT | PRINT | IF | FOR | VARIABLE | RETURN | DECLARATION ), "\n" ;
ASSIGNMENT = IDENTIFIER, ( "=", BOOLEXPRESSION | ARGS ) ;
ARGS = "(", ( λ | BOOLEXPRESSION, { ",", BOOLEXPRESSION } ), ")" ;
PRINT = "print", "(", BOOLEXPRESSION, ")" ;
IF = "if", BOOLEXPRESSION, ":", BLOCK, ( λ | "else", ":", BLOCK ) ;
FOR = "while", ASSIGNMENT, ";", BOOLEXPRESSION, ";", ASSIGNMENT, ":", BLOCK;
VARIABLE = TYPE, IDENTIFIER, ( λ | "=", BOOLEXPRESSION ) ;
RETURN = "return", BOOLEXPRESSION ;
BOOLEXPRESSION = BOOLTERM, { ( "or" ), BOOLTERM } ;
BOOLTERM = RELATIONALEXPRESSION, { ( "and" ), RELATIONALEXPRESSION } ;
RELATIONALEXPRESSION = EXPRESSION, { ( "==" | ">" | "<" ), EXPRESSION } ;
EXPRESSION = TERM, { ( "+" | "-" ), TERM } ;
TERM = FACTOR, { ( "*" | "/" ), FACTOR } ;
FACTOR = ( ( "+" | "-" | "not" ), FACTOR ) | NUMBER | "(", BOOLEXPRESSION, ")" | IDENTIFIER, ( λ | ARGS ) | SCAN | STRING ;
SCAN = "input", "(", ")" ;
IDENTIFIER = LETTER, { LETTER | DIGIT | "_" } ;
NUMBER = DIGIT, { DIGIT } ;
STRING = ("'" , { CHAR }, "'" | '"' , { CHAR }, '"' )
LETTER = ( a | ... | z | A | ... | Z ) ;
DIGIT = ( 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 0 ) ;
CHAR = ( LETTER | DIGIT | "_" | "+" | "-" | "*" | "/" | " " | "!" | "@" | "#" | "$" | "%" | "^" | "&" | "(" | ")" | "[" | "]" | "{" | "}" | "'" | "\"" | ":" | ";" | "," | "." | "?" | "=" ) ;
TYPE = ( "int" | "string" ) ;
TYPEVOID = ( "void" ) ;
```
