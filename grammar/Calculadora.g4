/******************************************************
 * A multi-line Javadoc-like comment about my grammar *
 ******************************************************/
grammar Calculadora;

stat:   expr NEWLINE
    |   ID '=' expr NEWLINE
    |   NEWLINE
    ;

expr:   expr op=(MUL|DIV) expr  #MulDiv
    |   expr op=(ADD|SUB) expr  #AddSub
    |   INT                     #int
    |   DOUBLE                  #double
    |   '(' expr ')'            #parens
    ;

NEWLINE :   [\r\n]+;
INT     :   [0-9]+;
DOUBLE  :   [0-9]+'.'[0-9]+;
ID      :   [a-zA-Z]+;

MUL : '*' ;
DIV : '/' ;
ADD : '+' ;
SUB : '-' ;

