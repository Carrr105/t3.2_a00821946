%{
    #include "y.tab.h"
%}

%%
program                     return PROGRAM;
var                         return VAR;
print                       return PRINT;
int                         return INT;
float                       return FLOAT;
if                          return IF;
else                        return ELSE;
[a-zA-Z][a-zA-Z_0-9]*       return ID;
";"                         return SEMICOLON;
"="                         return EQUALS;
"+"                         return PLUS;
"-"                         return MINUS;
"/"                         return DIVIDE;
"*"                         return MULTIPLY;
"("                         return OPENPARENTHESES;
")"                         return CLOSEPARENTHESES;
"."                         return DOT;
":"                         return TWODOTS;
"{"                         return OPENBRACE;
"}"                         return CLOSEBRACE;
"<>"                        return DIFFERENT;
">"                         return GREATER;
"<"                         return LESS;
\d+                         return CTEI;
\d+\.\d+                    return CTEF;
[a-zA-Z]+                   return CTESTRING;

[ \t\n]                     ;
%%

int yywrap(void){
    return 1;
}