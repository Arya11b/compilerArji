import ply.lex as lex
import re



class Lexer:
    token_list = [
        'TOKEN_ID',
        'TOKEN_INTEGER',
        'TOKEN_REAL',
        'TOKEN_STRING',
        'TOKEN_BITWISE_AND',
        'TOKEN_AND',
        'TOKEN_BITWISE_OR',
        'TOKEN_OR',
        'TOKEN_NOT',
        'TOKEN_BITWISE_NOT',
        'TOKEN_SHIFT_RIGHT',
        'TOKEN_SHIFT_LEFT',
        'TOKEN_ASSIGNMENT',
        'TOKEN_ADDITION',
        'TOKEN_SUBTRACTION',
        'TOKEN_MULTIPLICATION',
        'TOKEN_DIVISION',
        'TOKEN_MODULO',
        'TOKEN_POWER',
        'TOKEN_GT',
        'TOKEN_GE',
        'TOKEN_LT',
        'TOKEN_LE',
        'TOKEN_EQ',
        'TOKEN_NE',
        'TOKEN_LCB',
        'TOKEN_RCB',
        'TOKEN_LP',
        'TOKEN_RP',
        'TOKEN_DOT',
        'TOKEN_SEMICOLON',
        'TOKEN_COMMA',
        'TOKEN_COMMENT',
        'TOKEN_ERROR'
    ]
    reserved = {
        'class' : 'TOKEN_CLASS',
        'reference' : 'TOKEN_REFERENCE',
        'static' : 'TOKEN_STATIC',
        'int' : 'TOKEN_INT_TYPE',
        'real' : 'TOKEN_REAL_TYPE',
        'bool' : 'TOKEN_BOOL_TYPE',
        'string' : 'TOKEN_STRING_TYPE',
        'void' : 'TOKEN_VOID',
        'true' : 'TOKEN_TRUE',
        'false' : 'TOKEN_FALSE',
        'print' : 'TOKEN_PRINT',
        'return' : 'TOKEN_RETURN',
        'break' : 'TOKEN_BREAK',
        'continue' : 'TOKEN_CONTINUE',
        'if' : 'TOKEN_IF',
        'else': 'TOKEN_ELSE',
        'elseif' : 'TOKEN_ELSEIF',
        'while' : 'TOKEN_WHILE',
        'for' : 'TOKEN_FOR',
        'to' : 'TOKEN_TO',
        'in' : 'TOKEN_IN',
        'steps' : 'TOKEN_STEPS',
    }
    ids = []
    ints =[]
    reals = []
    strings=[]
    tokens = token_list + list(reserved.values())
    t_ignore = ' \t'
    def t_TOKEN_REAL(self,t):
        r'[\+-]?\b([1-9][0-9]*|0)\b\.\b([0-9]*[1-9]|0)\b'
        # r'(\+|-)?\b((([1-9][0-9]*)|0)(\.([0-9]*[1-9]|0)))\b|\b(\.([0-9]*[1-9]|0))\b'
        # r'\b((\+|-)?(([1-9][0-9]*)|0)?(\.([0-9]*[1-9]|0)))\b|\b((\+|-)?(([1-9][0-9]*)|0)(\.([0-9]*[1-9]|0)?))\b'
        self.reals.append(t.value)
        try:
            t.value = float(t.value)
        except:
            return self.t_error(t)
        # print(t.value)
        return t
    def t_TOKEN_INTEGER(self,t):
        # r'[\+-]?[0-9]+|[\+-]?0b[01]+|[\+-]?0x[0-9a-fA-F]+'
        r'[\+-]?\b([1-9][0-9]*|0b0|0x0|0b1[01]*|0x[1-9A-Fa-f][0-9a-fA-F]*|0)\b'
        self.ints.append(t.value)
        try:
            t.value = int(t.value,0)
        except:
            # print('error')
            return self.t_error(t)
        return t
    def t_TOKEN_ID(self,t):
        r'[a-zA-Z_][a-zA-Z_0-9]*'
        if len(t.value)%2==0:
            return self.t_error(t)
        i = 0
        while i < len(t.value):
            i = t.value.find('_',i)
            j = t.value.find('_',i+1)
            if j == -1:
                break
            if j - i !=2:
                return self.t_error(t)
            else:
                i = j
        self.ids.append(t.value)

        return t
    def t_TOKEN_COMMENT(self,t):
        r'/\*([^*]|[\r\n]|(\*+([^*/]|[\r\n])))*\*+/|//.*?\n'
        pass

    def t_TOKEN_STRING(self, t):
        r'"(.*?)(\s)*"((\s)*(\+(\s)*"(.*?)"))*'
        self.strings.append(t.value)
        l = re.split(r'[\n\s]',t.value)
        s=''
        # print(l)
        for x in l:
            if len(x)>1:
                if x[0] == '"' and x[-1] == '"':
                    s+=x[1:-1]
        t.value =s
        # print(t.value)
        return t
    def t_TOKEN_ERROR(self,t):
        r'[\w]+'
        return self.t_error(t)
    t_TOKEN_BITWISE_AND = r'&'
    t_TOKEN_AND = r'&&'
    t_TOKEN_BITWISE_OR = r'\|'
    t_TOKEN_OR = r'\|\|'
    t_TOKEN_NOT = r'\!'
    t_TOKEN_BITWISE_NOT = r'~'
    t_TOKEN_SHIFT_RIGHT = r'>>'
    t_TOKEN_SHIFT_LEFT = r'<<'
    t_TOKEN_ASSIGNMENT = r'='
    t_TOKEN_ADDITION = r'\+'
    t_TOKEN_SUBTRACTION = r'-'
    t_TOKEN_MULTIPLICATION = r'\*'
    t_TOKEN_DIVISION = r'/'
    t_TOKEN_MODULO = r'%'
    t_TOKEN_POWER = r'\^'
    t_TOKEN_GT = r'>'
    t_TOKEN_GE = r'>='
    t_TOKEN_LT = r'<'
    t_TOKEN_LE = r'<='
    t_TOKEN_EQ = r'=='
    t_TOKEN_NE = r'\!='
    t_TOKEN_LCB = r'\{'
    t_TOKEN_RCB = r'\}'
    t_TOKEN_LP = r'\('
    t_TOKEN_RP = r'\)'
    t_TOKEN_DOT = r'\.'
    t_TOKEN_SEMICOLON = r';'
    t_TOKEN_COMMA = r'\,'
    # t_TOKEN_ERROR = r'[\w]+'


    def t_newline(self,t):
        r'\n+'
        t.lexer.lineno += len(t.value)
    def t_error(self,t):
        # print("Illegal character '%s'" % t.value)
        # print('TOKEN_ERROR')
        t.value='-'
        t.lexer.skip(0)

    def build(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)
        return self.lexer

