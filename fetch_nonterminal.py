class NoneTerminal:

    def __init__(self, rule):
        self.rule = rule
        self.place = ""
        self.true_list = []
        self.false_list = []
        self.begin = ""
        self.type = ""
        self.exp = ""
        self.label = ""
        self.value = ""
        self.code = ''''''
        self.m = []
        self.quad = []
        self.parameters = []
        self.number = ""

    def get_value(self):
        if self.place == "EMPTY":
            return str(self.value)
        return str(self.place)
