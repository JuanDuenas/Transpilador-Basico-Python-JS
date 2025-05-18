lexer grammar Python3Lexer;

// Keywords - must come before NAME for precedence
DEF: 'def';
IF: 'if';
ELIF: 'elif';
ELSE: 'else';
RETURN: 'return';
AND: 'and';
OR: 'or';
NOT: 'not';

// Identifiers
NAME: [a-zA-Z_] [a-zA-Z0-9_]*;

// Literals
NUMBER: [0-9]+ ('.' [0-9]+)?;
STRING: '"' (~["\r\n])* '"' | '\'' (~['\r\n])* '\'';

// Operators
PLUS: '+';
MINUS: '-';
STAR: '*';
DIV: '/';
MOD: '%';
ASSIGN: '=';

// Comparison operators
LESS_THAN: '<';
GREATER_THAN: '>';
EQUALS: '==';
GT_EQ: '>=';
LT_EQ: '<=';
NOT_EQ: '!=';

// Punctuation
LPAREN: '(';
RPAREN: ')';
COLON: ':';
COMMA: ',';

// Whitespace and comments
NEWLINE: ('\r'? '\n' | '\r')+ -> channel(HIDDEN);
WS: [ \t]+ -> channel(HIDDEN);
COMMENT: '#' ~[\r\n]* -> channel(HIDDEN);
