from common import *


def check(input):
    string = []

    try:
        for i in input:
            string.append(Terminal(i))
    except ValueError:
        return False

    string.append(MARKER)
    stack = [MARKER]
    while True:
        if len(stack) == 1 and stack[0] == MARKER:
            stack.append(string[0])
            string = string[1:]

        if len(stack) == 2 and stack[-1] == START_SYMBOL:
            break

        rel = get_relation(stack[-1], string[0])

        if rel == RelType.less or rel == RelType.equal:
            stack.append(string[0])
            string = string[1:]
        elif rel == RelType.more:
            removed_symbols = []
            while True:
                curr_sym = stack.pop()
                removed_symbols.insert(0, curr_sym)
                if get_relation(stack[-1], curr_sym) == RelType.less:
                    break
            try:
                stack.append(collapse(removed_symbols))
            except ValueError:
                return False
    if stack[-1] == START_SYMBOL:
        return True
    else:
        return False
