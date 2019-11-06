from enum import Enum


class TokenType(Enum):

    # identify by TokenType(token)
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
    OP_ADD = '+'
    OP_MUL = '*'
    OP_DIV = '/'
    OP_LESS = '<'
    OP_MORE = '>'
    OP_EQUAL = '=='
    OP_SET = '='
    OP_SET_CYCLE = ':='

    # special ones
    # need to be identified manually
    OP_NEGATE = '[-]?'
    VARIABLE = '[a-zA-Z]+'
    NUMBER = '-?[0-9]+'


class Separators(Enum):
    # Default
    DEFAULT_LINE_END = '\n'
    DEFAULT_FILE_END = '\u0000'
    DEFAULT_LINE_TAB = '\t'
    DEFAULT_LINE = ' '
    # Custom
    COMMENT_BEGIN = '{'
    COMMENT_END = '}'
    CODE_BEGIN = '['
    CODE_END = ']'
    EXPRESSION_BEGIN = '('
    EXPRESSION_END = ')'
    VAR_DEFINITION = ','
    VAR_DEFINITION_END = ';'

    def __new__(cls, *values):
        obj = object.__new__(cls)
        # first value is canonical value
        obj._value_ = values[0]
        for other_value in values[1:]:
            cls._value2member_map_[other_value] = obj
        obj._all_values = values
        return obj

    def __repr__(self):
        return '<%s.%s: %s>' % (
            self.__class__.__name__,
            self._name_,
            ', '.join([repr(v) for v in self._all_values]),
        )


class PartOfProgram(Enum):
    NOT_STARTED = 0
    VARIABLES_DEFINITION = 1
    VAR = 2
    CODE = 3
    COMMENT = 4
    FINISHED = 5

# list of separators (Separator(Enum)) that are not supposed to be listed in final output/result
unprintable_seps = [Separators.COMMENT_BEGIN, Separators.COMMENT_END, Separators.DEFAULT_LINE_END, Separators.DEFAULT_LINE, Separators.DEFAULT_LINE_TAB]
