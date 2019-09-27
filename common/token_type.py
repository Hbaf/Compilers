from enum import Enum


class TokenType(Enum):

    KEY_WORD_VAR = 'var'
    KEY_WORD_FOR = 'for'
    KEY_WORD_DO = 'do'
    KEY_WORD_TO = 'to'
    SEP_LFT_SQR = '['
    SEP_RGHT_SQR = ']'
    SEP_LFT_RND = '('
    SEP_RGHT_RND = ')'
    SEP_LFT_FGR = '{'
    SEP_RGHT_FGR = '}'
    SEP_COMMA = ','
    SEP_SEMICOLON = ';'
    OP_SUB = '-'
    OP_NEGATE = '[-]?'
    OP_ADD = '+'
    OP_MUL = '*'
    OP_DIV = '/'
    OP_LESS = '<'
    OP_MORE = '>'
    OP_EQUAL = '=='
    OP_SET = '='
    OP_SET_CYCLE = ':='
    VARIABLE = '[a-zA-Z]+'
    NUMBER = '-?[0-9]+'
