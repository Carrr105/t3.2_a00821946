%{
    #include "y.tab.h"
%}

%%
program                     return PROGRAM;
var                         return VAR;
if                          return IF;
else                        return ELSE;
print                       return PRINT;
int                         return INT;
float                       return FLOAT;
[a-zA-Z][a-zA-Z_0-9]*       return ID;
";"                         return SEMICOLON;
"+"                         return PLUS;
"-"                         return MINUS;
"/"                         return DIVIDE;
"*"                         return MULTIPLY;
"="                         return EQUALS;
"("                         return OPENPARENTHESES;
")"                         return CLOSEPARENTHESES;
"."                         return DOT;
":"                         return TWODOTS;
"{"                         return OPENBRACE;
"}"                         return CLOSEBRACE;
"<>"                        return DIFFERENT;
">"                         return GREATER;
"<"                         return LESS;
0*([12]?[0-9]{1,4}|3(2(7(6[0-7]|[0-5][0-9])|[0-6][0-9]{2})|[0-1][0-9]{3}))              return CTEI;
[0-9]*([0-9]\.?|\.[0-9])[0-9]*([Ee][-+]?[0-9]+)      return CTEF;
\"(\\.|[^"\\])*\"           return CTESTRING;

[ \t\n]                     ;
%%

int yywrap(void){
    return 1;
}