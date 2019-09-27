from lexer.Lexer import Lexer
files = ['lang_example', 'lang_wrong_example']
for i in files:
    fr = open(i, 'r')
    text = fr.read()
    lexer = Lexer(text)
    fw = open(i + '_out', 'w')
    for j in lexer.parse():
        fw.write('{}\n'.format(j.to_string()))
