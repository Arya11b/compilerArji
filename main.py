from lexer import Lexer
import tabulate

data = ''' 

2 + 6
2 +6
- 5
'''
l = Lexer()
lexer = l.build()
lexer.input(data)

types = []
lexemes = []
attrs = []
while True:
    tok = lexer.token()
    # print(dir(tok))
    # break
    if not tok:
        break
    # print(tok.lexer,end='\t\t')
    if tok.type == 'TOKEN_ID':
        lexemes.append(tok.value)
        tok.value = 'Index_ID ' + str(l.ids.index(tok.value))
    elif tok.type == 'TOKEN_INTEGER':
        lexemes.append(l.ints.pop(0))
    elif tok.type == 'TOKEN_REAL':
        lexemes.append(l.reals.pop(0))
    elif tok.type == 'TOKEN_STRING':
        lexemes.append(l.strings.pop(0))
    else: lexemes.append(tok.value)
    types.append(tok.type)
    attrs.append(tok.value)
t = []
for i in range(len(lexemes)):
    t.append([lexemes[i],types[i],attrs[i]])
print(tabulate.tabulate(t,headers=['Lexemes','Types','Attributes']))