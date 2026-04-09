grammar SimpleC;

// ==========================================
// REGRAS SINTÁTICAS (PARSER) - Letra minúscula
// ==========================================

// O programa é uma ou mais declarações seguidas do fim do arquivo (EOF)
programa: declaracao+ EOF;

// Uma declaração tem um tipo, um ID, um '=', uma expressão matemática e um ';'
declaracao: TIPO ID ATRIBUICAO expressao PONTO_VIRGULA;

// Uma expressão é um número, podendo ser somado a outros números
expressao: NUMERO (SOMA NUMERO)*;

// ==========================================
// REGRAS LÉXICAS (LEXER) - Letra maiúscula
// ==========================================

TIPO: 'i' | 's';
ATRIBUICAO: '=';
SOMA: '+';
SUBTRACAO: '-';
PONTO_VIRGULA: ';';

// Identificadores (nomes de variáveis): começam com letra ou _, seguidos de letras, _ ou números
ID: [a-zA-Z_][a-zA-Z_0-9]*;

// Números inteiros
NUMERO: [0-9]+;

// Regra especial: O ANTLR deve ignorar espaços, tabs e quebras de linha
ESPACO: [ \t\r\n]+ -> skip;