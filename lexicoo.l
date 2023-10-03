%option noyywrap
%{
#include <stdio.h>
%}

delim [ \t\n]
ws {delim}+
letra [A-Za-z]
digito [0-9]
id ({letra}|{digito})+
numero {digito}+(\.{digito}+)?(E[+-]?{digito}+)?
select [Ss][Ee][Ll][Ee][Cc][Tt]
from [Ff][Rr][Oo][Mm]
where [Ww][Hh][Ee][Rr][Ee]

%%
{ws} {} // Ignorar espacios en blanco
{select} { printf("PC: %s\n", yytext); }
{from} { printf("PC: %s\n", yytext); }
{where} { printf("PC: %s\n", yytext); }
"<" { printf("OPREL: <\n"); }
"<=" { printf("OPREL: <=\n"); }
"=" { printf("OPREL: =\n"); }
"<>" { printf("OPREL: <>\n"); }
">" { printf("OPREL: >\n"); }
">=" { printf("OPREL: >=\n"); }
"," { printf("SIGNO: ,\n"); }
{id} {
    printf("ID: %s\n", yytext);
}
{numero} {
    printf("Numero: %s\n", yytext);
}
. { printf("Token desconocido: %s\n", yytext); }
%%

int main()
{
    FILE *yyin = fopen("texto.txt", "r");
    if (yyin == NULL) {
        fprintf(stderr, "No se pudo abrir el archivo de entrada.\n");
        return 1;
    }

    yyin = fopen("texto.txt", "r");
    yylex();
    fclose(yyin);
    return 0;
}
