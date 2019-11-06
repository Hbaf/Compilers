from enum import Enum


class RelType(Enum):
    no = 0
    equal = 1
    more = 2
    less = 3


class NonTerminal(Enum):
    S = 'S'
    B = 'B'
    R = 'R'
    K = 'K'
    A = 'A'


class Terminal(Enum):
    d = 'd'
    a = 'a'
    b = 'b'
    c = 'c'
    mark = '#'


grammar_symbols = {}
count = 0
for i in NonTerminal:
    grammar_symbols.update({i: count})
    count += 1
for i in Terminal:
    grammar_symbols.update({i: count})
    count += 1

rules = {
    str([NonTerminal.B, Terminal.d, NonTerminal.R]):    NonTerminal.S,
    str([NonTerminal.K, Terminal.d, NonTerminal.A]):    NonTerminal.S,
    str([NonTerminal.R]):                               NonTerminal.K,
    str([NonTerminal.A]):                               NonTerminal.B,
    str([Terminal.a, NonTerminal.A]):                   NonTerminal.R,
    str([Terminal.b, NonTerminal.A]):                   NonTerminal.R,
    str([Terminal.c]):                                  NonTerminal.R,
    str([Terminal.b, NonTerminal.R]):                   NonTerminal.A,
    str([Terminal.c, NonTerminal.R]):                   NonTerminal.A,
    str([Terminal.a]):                                  NonTerminal.A
}
relTable = {
    (NonTerminal.B, Terminal.d):    RelType.equal,
    (NonTerminal.B, Terminal.d):    RelType.equal,
    (NonTerminal.R, Terminal.d):    RelType.more,
    (NonTerminal.K, Terminal.d):    RelType.equal,
    (NonTerminal.A, Terminal.d):    RelType.more,
    (Terminal.d, NonTerminal.R):    RelType.equal,
    (Terminal.d, NonTerminal.A):    RelType.equal,
    (Terminal.d, Terminal.a):       RelType.less,
    (Terminal.d, Terminal.b):       RelType.less,
    (Terminal.d, Terminal.c):       RelType.less,
    (Terminal.a, NonTerminal.A):    RelType.equal,
    (Terminal.a, Terminal.d):       RelType.more,
    (Terminal.a, Terminal.a):       RelType.less,
    (Terminal.a, Terminal.b):       RelType.less,
    (Terminal.a, Terminal.c):       RelType.less,
    (Terminal.b, NonTerminal.R):    RelType.equal,
    (Terminal.b, NonTerminal.A):    RelType.equal,
    (Terminal.b, Terminal.a):       RelType.less,
    (Terminal.b, Terminal.b):       RelType.less,
    (Terminal.b, Terminal.c):       RelType.less,
    (Terminal.c, NonTerminal.R):    RelType.equal,
    (Terminal.c, Terminal.d):       RelType.more,
    (Terminal.c, Terminal.a):       RelType.less,
    (Terminal.c, Terminal.b):       RelType.less,
    (Terminal.c, Terminal.c):       RelType.less
}
MARKER = Terminal('#')
START_SYMBOL = NonTerminal.S


def is_input_valid(string):
    if len(string) == 0:
        return False
    return True


def collapse(symbols):
    if str(symbols) in rules.keys():
        return rules.get(str(symbols))
    else:
        raise ValueError


def get_relation(a, b):
    if a == MARKER:
        return RelType.less
    if b == MARKER:
        return RelType.more
    return relTable.get((a, b))
