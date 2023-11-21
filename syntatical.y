%{
#include <stdio.h>
extern int yylex();
extern FILE* yyin;
void yyerror(const char *s);
%}

%union{
    int num;
    char *str;
}

%token FUNC IF ELSE FOR WHILE RETURN CHARACTER ADVANTAGE CHECKIT PRINT
%token SCANTEXT SCANNUMBER RANDOM CHECKADV CHECKST TYPE INT ITEMS
%token OR AND NOT EQUAL GREATER LESS PLUS MINUS DOT TIMES DIVIDE
%token LPAREN RPAREN LBRACE RBRACE SEMICOLON COMMA EXCLAMATION
%token AT HASH DOLLAR PERCENT CARET AMPERSAND LBRACKET RBRACKET COLON
%token APOSTROPHE QUOTE QUESTION ASSIGN ENTER IDENTIFIER NUMBER STRING

%left OR
%left AND
%left NOT
%left EQUAL GREATER LESS
%left PLUS MINUS DOT
%left TIMES DIVIDE
%left UMINUS

%%
program: /* empty */
       | declaration
       ;

declaration: FUNC IDENTIFIER LPAREN declaration_args RPAREN TYPE block ENTER
           ;

declaration_args: /* empty */
        | argument declaration_args
        | COMMA argument
        ;

argument: IDENTIFIER TYPE
        ;

block: LBRACE statement_list RBRACE ;

statement_list: /* empty */
              | statement
              ;

statement: assignment
         | print
         | if
         | for
         | while
         | variable
         | return
         | creation
         | createadvantage
         | checkitems
         ;

assignment: IDENTIFIER boolexpression_or_args ;

boolexpression_or_args: ASSIGN boolexpression
		      | boolexpression args
		      ;

args: LPAREN arg_list RPAREN
    ;

arg_list: /* empty */
        | boolexpression arg_list
        | COMMA boolexpression
        ;

print: PRINT LPAREN boolexpression RPAREN ;

checkitems: CHECKIT LPAREN RPAREN ;

if: IF boolexpression block
   | IF boolexpression block ELSE block
   ;

for: FOR assignment SEMICOLON boolexpression SEMICOLON assignment block ;

while: WHILE boolexpression block ;

variable: TYPE IDENTIFIER
         | TYPE IDENTIFIER ASSIGN boolexpression
         ;

return: RETURN boolexpression ;

creation: CHARACTER IDENTIFIER LPAREN TYPE IDENTIFIER SEMICOLON TYPE IDENTIFIER SEMICOLON TYPE IDENTIFIER RPAREN ;

createadvantage: ADVANTAGE LPAREN IDENTIFIER COMMA IDENTIFIER RPAREN ;

boolexpression: boolterm
              | boolterm OR boolterm
              ;

boolterm: relationalexpression
        | relationalexpression AND relationalexpression
        ;

relationalexpression: expression
                    | expression EQUAL expression
                    | expression GREATER expression
                    | expression LESS expression
                    ;

expression: term
          | term PLUS term
          | term MINUS term
          | term DOT term
          ;

term: factor
    | factor TIMES factor
    | factor DIVIDE factor
    ;

factor: PLUS factor 
      | MINUS factor 
      | NOT factor
      | NUMBER
      | LPAREN boolexpression RPAREN
      | IDENTIFIER args
      | STRING
      | functions
      ;

functions: SCANTEXT LPAREN RPAREN
         | SCANNUMBER LPAREN RPAREN
         | RANDOM LPAREN NUMBER RPAREN
         | CHECKADV LPAREN IDENTIFIER COMMA IDENTIFIER RPAREN
         | CHECKST LPAREN IDENTIFIER COMMA IDENTIFIER RPAREN
         ;

%%

void yyerror(const char* s) {
    fprintf(stderr, "%s\n", s);
}

int main(int argc, char **argv)
{
    FILE* file = fopen(argv[1], "r");
    if (!file) {
        fprintf(stderr, "Error opening file: %s\n", argv[1]);
        return 1;
    }

    yyin = file;

    yyparse();

    fclose(file);
    return 0;
}


