from lexer.lexer_result import *
from common.common import *


class Lexer:

    def __init__(self, text):
        self.text = text
        self.line_num = 1
        self.line_pos = 1
        self.text_pos = 0
        self.char = self.text[0]
        self.state = PartOfProgram.NOT_STARTED
        self.buffer = ''
        self.result = []

    def parse(self):
        while True:
            try:
                sep = Separators(self.char)
                self.pre_analyze()
                # end of file
                if sep == Separators.DEFAULT_FILE_END:
                    break
                # comment's beginning
                elif sep == Separators.COMMENT_BEGIN:
                    self.state = PartOfProgram.COMMENT
                # comment's ending
                elif sep == Separators.COMMENT_END:
                    self.state = PartOfProgram.CODE
                # not a comment section, not one of unprintable separators
                if self.state != PartOfProgram.COMMENT and sep not in unprintable_seps:
                    self.buffer += self.char
                    self.pre_analyze()
                self.next_char()
                continue
            except ValueError:  # not a separator
                pass
            if self.state != PartOfProgram.COMMENT:  # not a comment section
                self.buffer += self.char
            self.next_char()
        return self.result

    def analyze(self, lexeme):
        if len(lexeme) > 0:
            # checking if token matches predefined TokenType patterns, if no - check other variants
            try:
                self.result.append(Token(self.line_num, self.line_pos, TokenType(lexeme.lower()), lexeme))
            except ValueError:
                # check if token is variable(named only with letters)
                if lexeme.isalpha():
                    self.result.append(Token(self.line_num, self.line_pos, TokenType.VARIABLE, lexeme))
                # check if token is number(contains only digits)
                elif lexeme.isdigit():
                    self.result.append(Token(self.line_num, self.line_pos, TokenType.NUMBER, hex(int(lexeme))))
                # check if token is negative number
                elif len(lexeme) > 1 and lexeme[0] == '-' and lexeme[1:].isdigit():
                    self.result.append(Token(self.line_num, self.line_pos, TokenType.OP_NEGATE, '-'))
                    self.increase_line_pos(1)
                    self.analyze(lexeme[1:])
                    self.decrease_line_pos(1)
                else:
                    self.result.append(self.error(ErrorType.UNRECGN_TOKEN, lexeme))
                    self.increase_line_pos(len(lexeme))

    # special method made for correct counting line position of token
    # moves cursor to beginning of token
    def pre_analyze(self):
        self.decrease_line_pos(len(self.buffer))
        self.analyze(self.buffer)
        self.increase_line_pos(len(self.buffer))
        self.buffer = ''

    def increase_line_pos(self, length):
        self.line_pos = self.line_pos + length

    def decrease_line_pos(self, length):
        self.line_pos = self.line_pos - length

    def next_char(self):
        if self.char == '\n':
            self.line_num += 1
            self.line_pos = 0
        self.line_pos += 1
        self.text_pos += 1
        if self.text_pos == len(self.text):
            self.char = Separators.DEFAULT_FILE_END
        else:
            self.char = self.text[self.text_pos]

    def error(self, type, value):
        return Error(self.line_num, self.line_pos,
                     '{:<20}\t{:<20}'.format(type.value + ' :', value))
