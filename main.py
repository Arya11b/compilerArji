from lexer import Lexer
from yacc import Yacc
import tabulate
data = '''
reference "Number.shl"
class Program{
	string str = "string";
	real numbere;

	static void maine(){
		if(1){
			int num1r;

			if(2){
				int num2t;
			}

			while(true){
				bool boolean = false;
			}
		}
	}

	static int add(int a, int b){
		return a + b;
	}
}
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

y = Yacc()
# Build the parser

parser = y.build()

result = parser.parse(data)
print(result)

# for i in range(len(lexemes)):
#     t.append([lexemes[i],types[i],attrs[i]])
# print(tabulate.tabulate(t,headers=['Lexemes','Types','Attributes']))