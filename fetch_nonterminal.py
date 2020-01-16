class NoneTerminal:

    def __init__(self, rule):
        self.rule = rule
        self.place = ""
        self.true = ""
        self.false = ""
        self.begin = ""
        self.type = ""
        self.exp = ""
        self.label = ""
        self.value = ""
        self.code = ''''''
        self.quad = []
        self.parameters = []
        self.number = ""

    def get_value(self):
        if self.place == "EMPTY":
            return str(self.value)
        return str(self.place)
