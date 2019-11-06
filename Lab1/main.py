from grammar_checker import check
from common import *
while True:
    string = input()
    if is_input_valid(string) and check(string):
        print('String is correct')
    else:
        print('String is not part of grammar')
