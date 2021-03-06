from lexer import Lexer
from yacc import Yacc
# from parser_test import Parser as Yacc
import tabulate
phase_2_test_data = '''
reference "Number.shl"

class Program{
  string str = "string";
  real numbere;
  
  static void maine(){
    if(1){
      int _num1;
      
      if(2){
        int _num2;
      }
      
      while(true){
        int _num3;
      }
    }
  }
  
    static void abc(){
        int _num4;
    }
  
  static int add(int a, int b){
    return a + b;
  }
}
 '''
empty_data = ''
test = '''
class Program{
  static void maine(){
        int a = 3;
        int b = 4 * a;
        int var = a/ (-b + 32 << 2);
    }
}
'''
data = test
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

parser.parse(data)
print(y.codes)
# for i in range(len(lexemes)):
#     t.append([lexemes[i],types[i],attrs[i]])
# print(tabulate.tabulate(t,headers=['Lexemes','Types','Attributes']))