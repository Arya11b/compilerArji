import shlex
class Lexer:
    def __int__(self):
        self.read_file()
    def read_file(self):
        f = open("code.arji", "r")