import random

from fetch_nonterminal import NoneTerminal
from register import Register


def four_operation_code(p, cl):
    p[0] = NoneTerminal(p)
    reg = Register('real')
    p[0].place = reg.place
    temp1 = ''
    temp2 = ''
    print('this p1')
    print(p[1])
    if p[1].place != '':
        temp1 = p[1].place
    else:
        temp1 = p[1].value
    if p[3].place != '':
        temp2 = p[3].place
    else:
        temp2 = p[3].value
    # p[0].code = p[1].code + p[3].code +  p[0].place + " = " + p[1].value + " " + p[2] + " " + p[3].value() + ";\n"
    p[0].code = p[0].place + " = " + temp1 + " " + p[2] + " " + temp2 + ";"
    # if p[3].value!='' and p[1].value!='':
    #     if p[2] == '*':
    #         print('sss')
    #         print(int(p[1].value) * int(p[3].value))
    #         p[0].value = str(int(p[1].value) * int(p[3].value))
    #     elif p[2] == '+':
    #         p[0].value = str(int(p[1].value) + int(p[3].value))
    #     elif p[2] == '-':
    #         p[0].value = str(int(p[1].value) - int(p[3].value))
    #     elif p[2] == '/':
    #         p[0].value = str(int(p[1].value) / int(p[3].value))
    #     elif p[2] == '%':
    #         p[0].value = str(int(p[1].value) % int(p[3].value))
    #     elif p[2] == '^':
    #         p[0].value = str(int(p[1].value) ** int(p[3].value))
    #     elif p[2] == '|':
    #         p[0].value = str(int(p[1].value) | int(p[3].value))
    #     elif p[2] == '&':
    #         p[0].value = str(int(p[1].value) & int(p[3].value))
    #     elif p[2] == '<<':
    #         p[0].value = str(int(p[1].value) << int(p[3].value))
    #     elif p[2] == '>>':
    #         p[0].value = str(int(p[1].value) >> int(p[3].value))

    cl.append(p[0].code)
def three_operation_code(p, cl):
    p[0] = NoneTerminal(p)
    reg = Register('real')
    p[0].place = reg.place
    temp1 = ''
    if p[2].place != '':
        temp1 = p[2].place
    else:
        temp1 = p[2].value
    # p[0].code = p[1].code + p[3].code +  p[0].place + " = " + p[1].value + " " + p[2] + " " + p[3].value() + ";\n"
    p[0].code = p[0].place + " = " + p[1] + temp1 +  ";"
    if p[2].value!='':
        if p[1] == '~':
            p[0].value = str(~ int(p[2].value))
        elif p[1] == '-':
            p[0].value = str(- int(p[2].value))
        elif p[1] == '!':
            p2 = int(p[2].value)
            if p2 != 0:
                p[0].value = str(0)
            else:
                p[0].value = str(random.randint(1,30))
        print('++++')
        # print(p[0].value)
    cl.append(p[0].code)
def four_boolean_code(p,cl):
    p[0] = NoneTerminal(p)
    reg = Register('real')
    p[0].place = reg.place
    temp1 = ''
    temp2 = ''
    print('this p1')
    print(p[1])
    if p[1].place != '':
        temp1 = p[1].place
    else:
        temp1 = p[1].value
    if p[3].place != '':
        temp2 = p[3].place
    else:
        temp2 = p[3].value
    # p[0].code = p[1].code + p[3].code +  p[0].place + " = " + p[1].value + " " + p[2] + " " + p[3].value() + ";\n"
    p[0].code = p[0].place + " = " + temp1 + " " + p[2] + " " + temp2 + ";"
def pop_variable(variable):
    code = variable + " = *top; // pop { " + variable + " }\n"
    code += "top = top + 1;\n\n"
    return code
def load_all_registers(registers):
    code = "//^^^^^^^^^^^^^LOAD REGS^^^^^^^^^^^^^^^^^^^\n"
    for register in reversed(registers):
        code += pop_variable(register.place)
    code += "//^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n"
    return code
def load_all_variables(variables):
    code = "\n//^^^^^^^^^^^LOAD VARIBLES^^^^^^^^^^^^^^^^\n"
    for variable in reversed(variables):
        code += pop_variable(variable)
    code += "//^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\n"
    return code

