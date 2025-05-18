parser grammar Python3Parser;

options {
    tokenVocab = Python3Lexer;
}

// nueva regla raíz:
file_input
    : (funcdef | if_stmt | simple_stmt)* EOF
    ;
funcdef
    : 'def' NAME parameters ':' suite
    ;
if_stmt
    : 'if' test ':' suite ( 'elif' test ':' suite )* ( 'else' ':' suite )?
    ;

// Parameters for function definitions
parameters
    : '(' (typedargslist)? ')'
    ;

typedargslist
    : NAME (',' NAME)*
    ;

// Code blocks (suites) in Python
suite
    : simple_stmt 
    | statement+
    ;

simple_stmt
    : small_stmt
    ;

small_stmt
    : expr_stmt 
    | flow_stmt
    ;

expr_stmt
    : testlist
    | testlist '=' expr_stmt
    ;

flow_stmt
    : return_stmt
    ;

return_stmt
    : 'return' (testlist)?
    ;

statement
    : compound_stmt
    ;

compound_stmt
    : if_stmt 
    | funcdef
    ;

// Expressions and tests
test
    : or_test
    ;

or_test
    : and_test ('or' and_test)*
    ;

and_test
    : not_test ('and' not_test)*
    ;

not_test
    : 'not' not_test 
    | comparison
    ;

comparison
    : expr (comp_op expr)*
    ;

comp_op
    : '<' | '>' | '==' | '>=' | '<=' | '!='
    ;

expr
    : term (('+' | '-') term)*
    ;

term
    : factor (('*' | '/' | '%') factor)*
    ;

factor
    : ('+' | '-') factor 
    | atom
    ;

atom
    : NAME 
    | NUMBER 
    | STRING 
    | '(' test ')'
    ;

testlist
    : test (',' test)* (',')?
    ;
