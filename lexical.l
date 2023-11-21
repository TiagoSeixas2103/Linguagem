%{
#include "syntatical.tab.h"
%}

%option noyywrap

%%
"//".*      /* skip comments */ 
"func"      { return FUNC; }
"if"        { return IF; }
"else"      { return ELSE; }
"for"       { return FOR; }
"while"     { return WHILE; }
"return"    { return RETURN; }
"character" { return CHARACTER; }
"advantage" { return ADVANTAGE; }
"checkIt"   { return CHECKIT; }
"print"     { return PRINT; }
"scanText"  { return SCANTEXT; }
"scanNumber" { return SCANNUMBER; }
"random"    { return RANDOM; }
"checkAdv"  { return CHECKADV; }
"checkSt"   { return CHECKST; }
"type"      { return TYPE; }
"int"       { return INT; }
"items"     { return ITEMS; }
"or"        { return OR; }
"and"       { return AND; }
"not"       { return NOT; }
"=="        { return EQUAL; }
">"         { return GREATER; }
"<"         { return LESS; }
"+"         { return PLUS; }
"-"         { return MINUS; }
"."         { return DOT; }
"*"         { return TIMES; }
"/"         { return DIVIDE; }
"("         { return LPAREN; }
")"         { return RPAREN; }
"{"         { return LBRACE; }
"}"         { return RBRACE; }
";"         { return SEMICOLON; }
","         { return COMMA; }
"!"         { return EXCLAMATION; }
"@"         { return AT; }
"#"         { return HASH; }
"$"         { return DOLLAR; }
"%"         { return PERCENT; }
"^"         { return CARET; }
"&"         { return AMPERSAND; }
"["         { return LBRACKET; }
"]"         { return RBRACKET; }
":"         { return COLON; }
"'"         { return APOSTROPHE; }
"\""        { return QUOTE; }
";"         { return SEMICOLON; }
"."         { return DOT; }
"?"         { return QUESTION; }
"="         { return ASSIGN; }
"\n"        { return ENTER; }
[ \t]+    ; /* skip whitespace */
[a-zA-Z][a-zA-Z0-9]* { yylval.str = strdup(yytext); return IDENTIFIER; }
[0-9]+      { yylval.num = atoi(yytext); return NUMBER; }
\"(\\.|[^\"])*\" { yylval.str = strdup(yytext); return STRING; }
.           { printf("Unknown token"); yyterminate(); }
%%
