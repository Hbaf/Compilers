from enum import Enum

class Token:

    def __init__(self, line, pos, token_type, value='!'):
        self.line = line
        self.pos = pos
        self.type = token_type
        self.value = value

    def to_string(self):
        res = '{:>6}\t{:>6}\t{:<20}'.format(str(self.line), str(self.pos), str(self.type.name))
        if self.value != '!':
            res += '\t' + str(self.value)
        return res


class Error:

    def __init__(self, line, pos, message):
        self.line = line
        self.pos = pos
        self.message = message

    def to_string(self):
        res = '{:>6}\t{:>6}\t{:<55}'.format(str(self.line), str(self.pos), str(self.message))
        return res

class ErrorType(Enum):
    UNRECGN_TOKEN = 'Unrecognised token'
    UNEXPCT_TOKEN = 'Unexpected token'
    NO_XPCT_TOKEN = 'Expected token not found'
    UNDEFINED_VAR = 'Undefined variable'
