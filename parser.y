%{
  void yyerror(const char *s);
  #include <stdio.h>
  #include <stdlib.h>
  extern FILE* yyin;
  int yylex();
%}

%token PROGRAM VAR PRINT INT FLOAT
%token IF ELSE ID SEMICOLON PLUS MINUS DIVIDE MULTIPLY EQUALS
%token OPENPARENTHESES CLOSEPARENTHESES DOT TWODOTS
%token OPENBRACE CLOSEBRACE DIFFERENT GREATER LESS CTEF CTEI CTESTRING

%start programa

%%

programa: PROGRAM ID SEMICOLON vars bloque
    | PROGRAM ID SEMICOLON vars
    | PROGRAM ID SEMICOLON bloque
    | PROGRAM ID SEMICOLON
    ;

vars: VAR varsP
    ;

varsP: ID TWODOTS tipo SEMICOLON
    | ID TWODOTS tipo SEMICOLON varsP
    | ID DOT varsP
    ;

tipo: INT
    | FLOAT
    ;

bloque: OPENBRACE bloqueP CLOSEBRACE
    ;

bloqueP: estatuto
    | estatuto bloqueP
    | empty
    ;

estatuto: asignacion
    | condicion
    | escritura
    ;

asignacion: ID EQUALS expresion SEMICOLON
    ;

expresion: exp expresionP
    ;

expresionP: GREATER exp
    | LESS exp
    | DIFFERENT exp
    | empty
    ;

condicion: condicionP bloque SEMICOLON
    | condicionP bloque ELSE bloque SEMICOLON
    ;

condicionP: IF OPENPARENTHESES expresion CLOSEPARENTHESES
    ;

escritura: PRINT OPENPARENTHESES escrituraP CLOSEPARENTHESES SEMICOLON
    ;

escrituraP: expresion
    | expresion DOT escrituraP
    | CTESTRING
    | CTESTRING DOT
    ;

exp: termino expP
    ;

expP: PLUS exp
    | MINUS exp
    | empty
    ;

termino: factor terminoP
    ;

terminoP: MULTIPLY terminoP
    | DIVIDE terminoP
    | empty
    ;

factor: OPENPARENTHESES expresion CLOSEPARENTHESES
    | factorP
    ;

factorP: PLUS varcte
    | MINUS varcte
    | varcte
    ;

varcte: ID
    | CTEI
    | CTEF
    ;

empty:;
    


%%

int main() {
  yyin = fopen("test_fail.txt", "r");
  yyparse();
  fclose(yyin);
  return 0;
}

void yyerror(const char* s) {
	fprintf(stderr, "Parse error: %s\n", s);
	exit(1);
}