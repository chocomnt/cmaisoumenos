grammar cmaismenos;

// ==========================================
// REGRAS SINTÁTICAS (PARSER) - Letra minúscula
// ==========================================

// O programa é uma sequência de comandos
programa: comando* EOF;

// Comandos: declarações, entrada/saída, controle de fluxo, atribuições
comando: declaracao | entrada | saida | condicional | repeticao | atribuicao;

// Atribuição simples
atribuicao: ID ATRIBUICAO expressao PONTO_VIRGULA;

// Declarações
declaracao: declaracaoInt | declaracaoStr;
declaracaoInt: TIPO_INT ID ATRIBUICAO expressao PONTO_VIRGULA;
declaracaoStr: TIPO_STR ID ATRIBUICAO STRING PONTO_VIRGULA;

// Entrada/saída
entrada: RD ABRE_PARENTESES ID FECHA_PARENTESES PONTO_VIRGULA;
saida: PT ABRE_PARENTESES (expressao | STRING) FECHA_PARENTESES PONTO_VIRGULA;

// Controle de fluxo
condicional: IF expressaoLogica bloco (EL bloco)? (EI expressaoLogica bloco)*;
repeticao: WL expressaoLogica DO bloco;

// Bloco de comandos
bloco: ABRE_CHAVES comando* FECHA_CHAVES;

// Expressões aritméticas com parênteses
expressao: termo ((SOMA | SUBTRACAO) termo)*;
termo: fator ((MULTIPLICACAO | DIVISAO) fator)*;
fator: NUMERO | ID | ABRE_PARENTESES expressao FECHA_PARENTESES;

// Expressões lógicas
expressaoLogica: termoLogico ((AND | OR) termoLogico)*;
termoLogico: NOT? (comparacao | ABRE_PARENTESES expressaoLogica FECHA_PARENTESES);
comparacao: expressao IGUAL expressao | expressao MENOR expressao | expressao MAIOR expressao;

// ==========================================
// REGRAS LÉXICAS (LEXER) - Letra maiúscula
// ==========================================

TIPO_INT: 'i';
TIPO_STR: 's';
IGUAL: '==';
ATRIBUICAO: '=';
SOMA: '+';
SUBTRACAO: '-';
MULTIPLICACAO: '*';
DIVISAO: '/';
PONTO_VIRGULA: ';';
ABRE_PARENTESES: '(';
FECHA_PARENTESES: ')';
ABRE_CHAVES: '{';
FECHA_CHAVES: '}';

// Entrada/saída
RD: 'rd';
PT: 'pt';

// Controle de fluxo
IF: 'if';
EL: 'el';
EI: 'ei';
DO: 'do';
WL: 'wl';

// Operadores lógicos
AND: 'and';
OR: 'or';
NOT: '!';
MENOR: '<';
MAIOR: '>';

// Literais
STRING: '"' (~["\r\n])* '"';
ID: [a-zA-Z_][a-zA-Z_0-9]*;
NUMERO: [0-9]+;

// Comentários
COMENTARIO_LINHA: '#' ~[\r\n]* -> skip;
COMENTARIO_BLOCO: '###' .*? '###' -> skip;

// Espaços
ESPACO: [ \t\r\n]+ -> skip;