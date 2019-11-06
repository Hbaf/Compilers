from lexer.Lexer import Lexer
from argparse import ArgumentParser

parser = ArgumentParser(description='Simply returns in program lexeme usage table')
parser.add_argument('-f', type=str, dest='file', required=True, help='File to read program from')
args = parser.parse_args()
file = args.file
try:
    fr = open(file, 'r')
    text = fr.read()
    lexer = Lexer(text)
    fw = open(file + '_out', 'w')
    for j in lexer.parse():
        fw.write('{}\n'.format(j.to_string()))
except FileNotFoundError:
    print("There is no such file : %s" % format(file))
