from lexer.lexer_result import *
from common.part_of_programm import Part_of_programm as Part
from common.token_type import TokenType

EOF = '\u0000'


class Lexer:

    def __init__(self, text):
        self.text = text
        self.line_num = 1
        self.line_pos = 1
        self.text_pos = 0
        self.char = self.text[0]
        self.state = Part.NOT_STARTED
        self.prev_state = Part.NOT_STARTED
        self.buffer = ''
        self.result = []

    def parse(self):
        self.prev_state = Part.VARIABLES_DEFINITION
        self.state = Part.VARIABLES_DEFINITION

        while True:
            if self.char == '\n':
                self.pre_analyze(self.buffer)
                self.buffer = ''
            elif self.state == Part.VARIABLES_DEFINITION:
                if self.char == '[':
                    self.state = Part.CODE
                elif self.char == '{':
                    self.buffer = ''
                    self.state = Part.COMMENT
                    self.prev_state = Part.VARIABLES_DEFINITION

                if self.char not in [' ', '{', EOF]:
                    self.buffer += self.char
                else:
                    self.pre_analyze(self.buffer)
                    self.buffer = ''

            elif self.state == Part.VAR:
                if self.char == ';':
                    self.state = Part.VARIABLES_DEFINITION

            elif self.state == Part.CODE:
                if self.char == '{':
                    self.buffer = ''
                    self.state = Part.COMMENT
                    self.prev_state = Part.CODE
                elif self.char == ']':
                    self.state = Part.FINISHED

                if self.char not in [' ', '{', EOF]:
                    self.buffer += self.char
                else:
                    self.pre_analyze(self.buffer)
                    self.buffer = ''

            elif self.state == Part.COMMENT:
                if self.char == '}':
                    self.state = self.prev_state

            if self.char == EOF:
                self.pre_analyze(self.buffer)
                break

            self.next_char()
        return self.result

    def analyze(self, lexeme):
        if len(lexeme) > 0:
            if len(lexeme) > 1 and lexeme[-1] in ',;)]':  # check if two tokens are not splitted
                self.analyze(lexeme[:-1])
                self.analyze(lexeme[-1])
            elif len(lexeme) > 1 and lexeme[0] in '([':  # check if two tokens are not splitted
                self.analyze(lexeme[0])
                self.analyze(lexeme[1:])
            else:
                try:  # checking if token matches predefined TokenType patterns, if no - check other variants
                    self.result.append(Token(self.line_num, self.line_pos, TokenType(lexeme.lower()), lexeme))
                    self.increase_line_pos(len(lexeme))
                except ValueError:
                    if lexeme.isalpha():  # check if token is variable(named only with letters)
                        self.result.append(Token(self.line_num, self.line_pos, TokenType.VARIABLE, lexeme))
                        self.increase_line_pos(len(lexeme))
                    elif lexeme.isdigit():  # check if token is number(contains only digits)
                        self.result.append(Token(self.line_num, self.line_pos, TokenType.NUMBER, hex(int(lexeme))))
                        self.increase_line_pos(len(lexeme))
                    elif len(lexeme) > 1 and lexeme[0] == '-' and lexeme[1:].isdigit():  # check if token is a negative number(-number)
                        self.result.append(Token(self.line_num, self.line_pos, TokenType.OP_NEGATE, '-')) # analyze separtely minus
                        self.increase_line_pos(len(lexeme[0]))
                        self.analyze(lexeme[1:])                                                          #and number
                    else:
                        self.result.append(self.error(ErrorType.UNRECGN_TOKEN, lexeme))
                        self.increase_line_pos(len(lexeme))

    def pre_analyze(self, lexeme):
        self.line_pos = self.line_pos - len(lexeme)
        self.analyze(lexeme)

    def increase_line_pos(self, len):
        self.line_pos = self.line_pos + len

    def next_char(self):
        if self.char == '\n':
            self.line_num += 1
            self.line_pos = 0
        self.line_pos += 1
        self.text_pos += 1
        if self.text_pos == len(self.text):
            self.char = EOF
        else:
            self.char = self.text[self.text_pos]

    def error(self, type, value):
        return Error(self.line_num, self.line_pos,
                     '{:<20}\t{:<20}'.format(type.value + ' :', value))
