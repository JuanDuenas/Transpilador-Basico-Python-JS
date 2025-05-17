grammar Python;

// Creacion de gramatica simple que puede mantener una sintaxis basica de Python
/* 
 * Esta gramatica incluye reglas como:
 *  - Variable declarations and assignments
 *  - Basic arithmetic expressions
 *  - Function definitions
 *  - Control structures (if statements, loops)
 *  - Basic Python syntax like indentation
*/
// Parser Rules
program
    : statement*
    ;

statement
    : simpleStatement NEWLINE
    | compoundStatement
    ;

simpleStatement
    : assignmentStatement
    | expressionStatement
    | returnStatement
    | PASS
    ;

compoundStatement
    : functionDef
    | ifStatement
    | whileStatement
    | forStatement
    ;

assignmentStatement
    : varAssignment
    ;

varAssignment
    : NAME '=' expression
    ;

expressionStatement
    : expression
    ;

returnStatement
    : 'return' expression?
    ;

functionDef
    : 'def' NAME '(' parameterList? ')' ':' NEWLINE INDENT statement+ DEDENT
    ;

parameterList
    : parameter (',' parameter)*
    ;

parameter
    : NAME ('=' expression)?
    ;

ifStatement
    : 'if' expression ':' NEWLINE INDENT statement+ DEDENT
      elseIfStatement*
      elseStatement?
    ;

elseIfStatement
    : 'elif' expression ':' NEWLINE INDENT statement+ DEDENT
    ;

elseStatement
    : 'else' ':' NEWLINE INDENT statement+ DEDENT
    ;

whileStatement
    : 'while' expression ':' NEWLINE INDENT statement+ DEDENT
    ;

forStatement
    : 'for' NAME 'in' expression ':' NEWLINE INDENT statement+ DEDENT
    ;

expression
    : orExpr
    ;

orExpr
    : andExpr ('or' andExpr)*
    ;

andExpr
    : notExpr ('and' notExpr)*
    ;

notExpr
    : 'not' notExpr
    | comparison
    ;

comparison
    : addExpr (compOp addExpr)*
    ;

compOp
    : '<'
    | '>'
    | '=='
    | '>='
    | '<='
    | '!='
    ;

addExpr
    : multExpr (addOp multExpr)*
    ;

addOp
    : '+'
    | '-'
    ;

multExpr
    : factor (multOp factor)*
    ;

multOp
    : '*'
    | '/'
    | '%'
    ;

factor
    : '+' factor
    | '-' factor
    | power
    ;

power
    : atom ('**' factor)?
    ;

atom
    : NAME 
    | NUMBER
    | STRING
    | 'True' 
    | 'False'
    | 'None'
    | '(' expression ')'
    | list
    | dict
    | functionCall
    ;

list
    : '[' (expression (',' expression)*)? ']'
    ;

dict
    : '{' (keyValuePair (',' keyValuePair)*)? '}'
    ;

keyValuePair
    : expression ':' expression
    ;

functionCall
    : NAME '(' argumentList? ')'
    ;

argumentList
    : argument (',' argument)*
    ;

argument
    : expression
    | NAME '=' expression
    ;

// Lexer Rules
NAME
    : [a-zA-Z_][a-zA-Z0-9_]*
    ;

NUMBER
    : INTEGER
    | FLOAT
    ;

INTEGER
    : [0-9]+
    ;

FLOAT
    : [0-9]+ '.' [0-9]*
    | '.' [0-9]+
    ;

STRING
    : '\'' ~['\r\n]* '\''
    | '"' ~["\r\n]* '"'
    ;

NEWLINE
    : ('\r'? '\n' SPACES?)
    ;

INDENT
    : '<INDENT>'  // This will be handled by a custom token stream
    ;

DEDENT
    : '<DEDENT>'  // This will be handled by a custom token stream
    ;

SPACES
    : [ \t]+
    ;

COMMENT
    : '#' ~[\r\n]* -> skip
    ;

PASS
    : 'pass'
    ;

WS
    : [ \t]+ -> skip
    ;

// Special rule for handling Python's indentation-based syntax
// Note: Python indentation rules are complex - in a real implementation 
// this would require a custom token stream or preprocessing step

