from lexer import Lexer

# Yacc example
import ply.yacc as yacc
# Get the token map from the lexer.  This is required.
class Yacc:
    l = Lexer()
    l.build()
    tokens = l.tokens

    def p_program(self, p):
        'program : macros classes'
        print('program : macros classes')

    def p_macros(self, p):
        'macros : macros macro'
        print('macros : macros macro')

    def p_macros_ep(self, p):
        'macros : '
        print('macros : ')

    def p_macro(self, p):
        'macro : reference'
        print('macro : reference')

    def p_reference(self, p):
        'reference : TOKEN_REFERENCE TOKEN_STRING'
        print('reference : TOKEN_REFERENCE TOKEN_STRING')

    def p_classes(self, p):
        'classes : classes class'
        print('classes : classes class')

    def p_classes_ep(self, p):
        'classes : '
        print('classes : ')

    def p_class(self, p):
        'class : TOKEN_CLASS TOKEN_ID TOKEN_LCB symbol_decs TOKEN_RCB'
        print('class : TOKEN_CLASS TOKEN_ID TOKEN_LCB symbol_decs TOKEN_RCB')

    def p_symbol_decs(self, p):
        'symbol_decs : symbol_decs symbol_dec'
        print('symbol_decs : symbol_decs symbol_dec')

    def p_symbol_decs_ep(self, p):
        'symbol_decs : '
        print('symbol_decs : ')

    def p_symbol_dec_var(self, p):
        'symbol_dec : var_dec'
        print('symbol_dec : var_dec')

    def p_symbol_dec_func(self, p):
        'symbol_dec : func_dec'
        print('symbol_dec : func_dec')

    def p_var_dec(self, p):
        'var_dec : var_type var_list TOKEN_SEMICOLON'
        print('var_dec : var_type var_list TOKEN_SEMICOLON')

    def p_var_type_return(self, p):
        'var_type : return_type'
        print('var_type : return_type')


    def p_var_type_static_return(self, p):
        'var_type : TOKEN_STATIC return_type'
        print('var_type : TOKEN_STATIC return_type')


    def p_return_type_int(self, p):
        'return_type : TOKEN_INT_TYPE'
        print('return_type : TOKEN_INT_TYPE')

    def p_return_type_real(self, p):
        'return_type : TOKEN_REAL_TYPE'
        print('return_type : TOKEN_REAL_TYPE')

    def p_return_type_bool(self, p):
        'return_type : TOKEN_BOOL_TYPE'
        print('return_type : TOKEN_BOOL_TYPE')

    def p_return_type_string(self, p):
        'return_type : TOKEN_STRING_TYPE'
        print('return_type : TOKEN_STRING_TYPE')

    def p_return_type_id(self, p):
        'return_type : TOKEN_ID'
        print('return_type : TOKEN_ID')

    def p_var_list_comma(self, p):
        'var_list : var_list TOKEN_COMMA var_list_item'
        print('var_list : var_list TOKEN_COMMA var_list_item')

    def p_var_list_var_list_item(self, p):
        'var_list : var_list_item'
        print('var_list : var_list_item')

    def p_var_list_item_id(self, p):
        'var_list_item : TOKEN_ID'
        print('var_list_item : TOKEN_ID')

    def p_var_list_item_assignment(self, p):
        'var_list_item : TOKEN_ID TOKEN_ASSIGNMENT exp'
        print('var_list_item : TOKEN_ID TOKEN_ASSIGNMENT exp')

    def p_func_dec(self, p):
        'func_dec : var_type func_body'
        print('func_dec : var_type func_body')

    def p_func_dec_void(self, p):
        'func_dec : TOKEN_VOID func_body'
        print('func_dec : TOKEN_VOID func_body')

    def p_func_dec_static_void(self, p):
        'func_dec : TOKEN_STATIC TOKEN_VOID func_body'
        print('func_dec : TOKEN_STATIC TOKEN_VOID func_body')

    def p_func_body(self, p):
        'func_body : TOKEN_ID TOKEN_LP formal_arguments TOKEN_RP block'
        print('func_body : TOKEN_ID TOKEN_LP formal_arguments TOKEN_RP block')

    def p_formal_arguments(self, p):
        'formal_arguments : formal_arguments_list'
        print('formal_arguments : formal_arguments_list')

    def p_formal_arguments_ep(self, p):
        'formal_arguments : '
        print('formal_arguments : ')

    def p_formal_arguments_list(self, p):
        'formal_arguments_list : formal_arguments_list TOKEN_COMMA formal_argument'
        print('formal_arguments_list : formal_arguments_list TOKEN_COMMA formal_argument')

    def p_formal_arguments_list_1(self, p):
        'formal_arguments_list : formal_argument'
        print('formal_arguments_list : formal_argument')

    def p_formal_argument(self, p):
        'formal_argument : return_type TOKEN_ID'
        print('formal_argument : return_type TOKEN_ID')


    def p_block(self, p):
        'block : TOKEN_LCB statements_list TOKEN_RCB'
        print('block : TOKEN_LCB statements_list TOKEN_RCB')

    def p_block_statement(self, p):
        'block : statement'
        print('block : statement')

    def p_statements_list(self, p):
        'statements_list : statements_list statement'
        print('statements_list : statements_list statement')

    def p_statements_list_ep(self, p):
        'statements_list : '
        print('statements_list : ')

    def p_statement_semicolon(self, p):
        'statement : TOKEN_SEMICOLON'
        print('statement : TOKEN_SEMICOLON')

    def p_statement_exp(self, p):
        'statement : exp TOKEN_SEMICOLON'
        print('statement : exp TOKEN_SEMICOLON')

    def p_statement_assignment(self, p):
        'statement : assignment'
        print('statement : assignment')

    def p_statement_print(self, p):
        'statement : print'
        print('statement : print')

    def p_statement_dec(self, p):
        'statement : statement_var_dec'
        print('statement : statement_var_dec')

    def p_statement_if(self, p):
        'statement : if'
        print('statement : if')

    def p_statement_for(self, p):
        'statement : for'
        print('statement : for')

    def p_statement_while(self, p):
        'statement : while'
        print('statement : while')

    def p_statement_return(self, p):
        'statement : return'
        print('statement : return')

    def p_statement_break(self, p):
        'statement : break'
        print('statement : break')

    def p_statement_continue(self, p):
        'statement : continue'
        print('statement : continue')

    def p_assignment(self, p):
        'assignment : lvalue TOKEN_ASSIGNMENT exp TOKEN_SEMICOLON'
        print('assignment : lvalue TOKEN_ASSIGNMENT exp TOKEN_SEMICOLON')

    def p_lvalue_id(self, p):
        'lvalue : TOKEN_ID'
        print('lvalue1 : TOKEN_ID')

    def p_lvalue_idid(self, p):
        'lvalue : TOKEN_ID TOKEN_DOT TOKEN_ID'
        print('lvalue : TOKEN_ID TOKEN_DOT TOKEN_ID')

    def p_print(self, p):
        'print : TOKEN_PRINT TOKEN_LP TOKEN_STRING TOKEN_RP TOKEN_SEMICOLON'
        print('print : TOKEN_PRINT TOKEN_LP TOKEN_STRING TOKEN_RP TOKEN_SEMICOLON')

    def p_statement_var_dec(self, p):
        'statement_var_dec : return_type var_list TOKEN_SEMICOLON'
        print('statement_var_dec : return_type var_list TOKEN_SEMICOLON')

    # def p_statement_var_dec_1(self, p):
    #     'statement_var_dec : lvalue1 var_list TOKEN_SEMICOLON'
    #     print('statement_var_dec : lvalue1 var_list TOKEN_SEMICOLON')

    def p_if(self, p):
        'if : TOKEN_IF TOKEN_LP exp TOKEN_RP block elseif_blocks else_block'
        print('if : TOKEN_IF TOKEN_LP exp TOKEN_RP block %prec TOKEN_IF')

    def p_elseif_blocks(self, p):
        'elseif_blocks : elseifs'
        print('elseif_blocks : elseifs')

    def p_elseif_blocks_ep(self, p):
        'elseif_blocks : '
        print('elseif_blocks : ')

    def p_elseifs(self, p):
        'elseifs : elseifs elseif'
        print('elseifs : elseifs elseif')

    def p_elseifs_ep(self, p):
        'elseifs : elseif'
        print('elseifs : elseif')

    def p_elseif(self, p):
        'elseif : TOKEN_ELSEIF TOKEN_LP exp TOKEN_RP block'
        print('elseif : TOKEN_ELSEIF TOKEN_LP exp TOKEN_RP block')

    def p_else_block(self,p):
        'else_block : TOKEN_ELSE block'
        print('else_block : TOKEN_ELSE block')

    def p_else_block_ep(self,p):
        'else_block : '
        print('else_block : ')

    def p_for(self, p):
        'for : TOKEN_FOR TOKEN_LP TOKEN_ID TOKEN_IN exp TOKEN_TO exp TOKEN_STEPS exp TOKEN_RP block'
        print('for : TOKEN_FOR TOKEN_LP TOKEN_ID TOKEN_IN exp TOKEN_TO exp TOKEN_STEPS exp TOKEN_RP block')

    def p_while(self, p):
        'while : TOKEN_WHILE TOKEN_LP exp TOKEN_RP block'
        print('while : TOKEN_WHILE TOKEN_LP exp TOKEN_RP block')

    def p_return(self, p):
        'return : TOKEN_RETURN exp TOKEN_SEMICOLON'
        print('return : TOKEN_RETURN exp TOKEN_SEMICOLON')

    def p_break(self, p):
        'break : TOKEN_BREAK TOKEN_SEMICOLON'
        print('break : TOKEN_BREAK TOKEN_SEMICOLON')

    def p_continue(self, p):
        'continue : TOKEN_CONTINUE TOKEN_SEMICOLON'
        print('continue : TOKEN_CONTINUE TOKEN_SEMICOLON')

    def p_exp_int(self, p):
        'exp : TOKEN_INTEGER'
        print('exp : TOKEN_INTEGER')

    def p_exp_real(self, p):
        'exp : TOKEN_REAL'
        print('exp : TOKEN_REAL')

    def p_exp_true(self, p):
        'exp : TOKEN_TRUE'
        print('exp : TOKEN_TRUE')

    def p_exp_false(self, p):
        'exp : TOKEN_FALSE'
        print('exp : TOKEN_FALSE')

    def p_exp_string(self, p):
        'exp : TOKEN_STRING'
        print('exp : TOKEN_STRING')

    def p_exp_lvalue(self, p):
        'exp : lvalue'
        print('exp : lvalue')

    def p_exp_binary_op(self, p):
        'exp : binary_operation'
        print('exp : binary_operation %prec BIOP')

    def p_exp_logical_op(self, p):
        'exp : logical_operation'
        print('exp : logical_operation')

    def p_exp_comparison_op(self, p):
        'exp : comparison_operation'
        print('exp : comparison_operation %prec COMOP')

    def p_exp_bitwise_op(self, p):
        'exp : bitwise_operation'
        print('exp : bitwise_operation %prec BITOP')

    def p_exp_unary_op(self, p):
        'exp : unary_operation'
        print('exp : unary_operation')

    def p_exp_lp_exp_rp(self, p):
        'exp : TOKEN_LP exp TOKEN_RP'
        print('exp : TOKEN_LP exp TOKEN_RP')

    def p_exp_func_call(self, p):
        'exp : function_call'
        print('exp : function_call')

    def p_binary_operation_add(self, p):
        'binary_operation : exp TOKEN_ADDITION exp '
        print('binary_operation : exp TOKEN_ADDITION exp ')

    def p_binary_operation_sub(self, p):
        'binary_operation : exp TOKEN_SUBTRACTION exp'
        print('binary_operation : exp TOKEN_SUBTRACTION exp')

    def p_binary_operation_mult(self, p):
        'binary_operation : exp TOKEN_MULTIPLICATION exp'
        print('binary_operation : exp TOKEN_MULTIPLICATION exp')

    def p_binary_operation_div(self, p):
        'binary_operation : exp TOKEN_DIVISION exp'
        print('binary_operation : exp TOKEN_DIVISION exp')

    def p_binary_operation_modulu(self, p):
        'binary_operation : exp TOKEN_MODULO exp'
        print('binary_operation : exp TOKEN_MODULO exp')

    def p_binary_operation_pow(self, p):
        'binary_operation : exp TOKEN_POWER exp'
        print('binary_operation : exp TOKEN_POWER exp')

    def p_binary_operation_shleft(self, p):
        'binary_operation : exp TOKEN_SHIFT_LEFT exp'
        print('binary_operation : exp TOKEN_SHIFT_LEFT exp')

    def p_binary_operation_shright(self, p):
        'binary_operation : exp TOKEN_SHIFT_RIGHT exp'
        print('binary_operation : exp TOKEN_SHIFT_RIGHT exp')

    def p_logical_operation_and(self, p):
        'logical_operation : exp TOKEN_AND exp'
        print('logical_operation : exp TOKEN_AND exp')

    def p_logical_operation_or(self, p):
        'logical_operation : exp TOKEN_OR exp'
        print('logical_operation : exp TOKEN_OR exp')

    def p_comparison_operation_lt(self, p):
        'comparison_operation : exp TOKEN_LT exp'
        print('comparison_operation : exp TOKEN_LT exp')

    def p_comparison_operation_le(self, p):
        'comparison_operation : exp TOKEN_LE exp'
        print('comparison_operation : exp TOKEN_LE exp')

    def p_comparison_operation_gt(self, p):
        'comparison_operation : exp TOKEN_GT exp'
        print('comparison_operation : exp TOKEN_GT exp')

    def p_comparison_operation_ge(self, p):
        'comparison_operation : exp TOKEN_GE exp'
        print('comparison_operation : exp TOKEN_GE exp')

    def p_comparison_operation_eq(self, p):
        'comparison_operation : exp TOKEN_EQ exp'
        print('comparison_operation : exp TOKEN_EQ exp')

    def p_comparison_operation_ne(self, p):
        'comparison_operation : exp TOKEN_NE exp'
        print('comparison_operation : exp TOKEN_NE exp')

    def p_bitwise_operation_bit_and(self, p):
        'bitwise_operation : exp TOKEN_BITWISE_AND exp'
        print('bitwise_operation : exp TOKEN_BITWISE_AND exp')

    def p_bitwise_operation_bit_or(self, p):
        'bitwise_operation : exp TOKEN_BITWISE_OR exp'
        print('bitwise_operation : exp TOKEN_BITWISE_OR exp')

    def p_unary_operation_mirror(self, p):
        'unary_operation : TOKEN_SUBTRACTION exp '
        print('unary_operation : TOKEN_SUBTRACTION exp %prec UMINUS')

    def p_unary_operation_not(self, p):
        'unary_operation : TOKEN_NOT exp'
        print('unary_operation : TOKEN_NOT exp')

    def p_unary_operation_bit_not(self, p):
        'unary_operation : TOKEN_BITWISE_NOT exp'
        print('unary_operation : TOKEN_BITWISE_NOT exp')

    def p_function_call_func2(self, p):
        'function_call : TOKEN_ID function_call_body'
        print('function_call : lvalue2 function_call_body')

    def p_function_call_func1(self, p):
        'function_call : TOKEN_ID TOKEN_DOT TOKEN_ID function_call_body'
        print('function_call : lvalue1 function_call_body')

    def p_function_call_body(self, p):
        'function_call_body : TOKEN_LP actual_arguments TOKEN_RP'
        print('function_call_body : TOKEN_LP actual_arguments TOKEN_RP')

    def p_actual_arguments(self, p):
        'actual_arguments : actual_arguments_list'
        print('actual_arguments : actual_arguments_list')
    def p_actual_arguments_ep(self, p):
        'actual_arguments : '
        print('actual_arguments : ')

    def p_actual_arguments_list_comma(self, p):
        'actual_arguments_list : actual_arguments_list TOKEN_COMMA exp'
        print('actual_arguments_list : actual_arguments_list TOKEN_COMMA exp')

    def p_actual_arguments_list_exp(self, p):
        'actual_arguments_list : exp'
        print('actual_arguments_list : exp')

    # def p_id_rule(self, p):
    #     'id_rule : ID'

    # def p_exp_plus2(self,p):
    #     'exp : exp term'
    #     p[0] = p[1] + p[2]
    #
    # def p_exp_plus(self, p):
    #     'exp : exp TOKEN_ADDITION term'
    #     p[0] = p[1] + p[3]
    #
    # def p_exp_minus(self,p):
    #     'exp : exp TOKEN_SUBTRACTION term'
    #     p[0] = p[1] - p[3]
    #
    # def p_exp_term(self,p):
    #     'exp : term'
    #     p[0] = p[1]
    #
    # def p_term_times(self,p):
    #     'term : term TOKEN_MULTIPLICATION factor'
    #     p[0] = p[1] * p[3]
    #
    # def p_term_div(self,p):
    #     'term : term TOKEN_DIVISION factor'
    #     p[0] = p[1] / p[3]
    #
    #
    # def p_term_factor(self,p):
    #     'term : factor'
    #     p[0] = p[1]
    #
    #
    # def p_factor_num(self,p):
    #     'factor : TOKEN_INTEGER'
    #     p[0] = p[1]
    #
    #
    # def p_factor_expr(self,p):
    #     'factor : TOKEN_LP exp TOKEN_RP'
    #     p[0] = p[2]
    #
    # Error rule for syntax errors
    def p_error(self,p):
        print("Syntax error in input!")
    def build(self, **kwargs):
        'build the parser'
        self.parser = yacc.yacc(module=self, **kwargs)
        return self.parser

    # precedence = (
    #     ('nonassoc', 'LVALI'),
    #     ('nonassoc', 'LVAL'),
    #     ('nonassoc', 'BIOP'),
    #     ('nonassoc', 'COMOP'),
    #     ('nonassoc', 'BITOP'),
    #     ('left', 'TOKEN_IF'),
    #     ('left', 'TOKEN_ELSEIF'),
    #     ('left', 'TOKEN_ELSE'),
    #     ('left', 'TOKEN_COMMA'),
    #     ('left', 'TOKEN_ASSIGNMENT'),
    #     ('left', 'TOKEN_OR'),
    #     ('left', 'TOKEN_AND'),
    #     ('left', 'TOKEN_NOT'),
    #     ('left', 'TOKEN_BITWISE_OR'),
    #     ('left', 'TOKEN_BITWISE_AND'),
    #     ('left', 'TOKEN_BITWISE_NOT'),
    #     ('left', 'TOKEN_LE', 'TOKEN_EQ', 'TOKEN_NE', 'TOKEN_GE', 'TOKEN_GT', 'TOKEN_LT'),
    #     ('left', 'TOKEN_SHIFT_LEFT', 'TOKEN_SHIFT_RIGHT'),
    #     ('left', 'TOKEN_ADDITION', 'TOKEN_SUBTRACTION'),
    #     ('left', 'TOKEN_MULTIPLICATION', 'TOKEN_DIVISION'),
    #     ('left', 'TOKEN_POWER'),
    #     ('left', 'TOKEN_MODULO'),
    #     ('left', 'UMINUS'),
    #     ('left', 'TOKEN_RP', 'TOKEN_LP')
    # )
y = Yacc()
# Build the parser
data = '''

 '''
parser = y.build()

result = parser.parse(data)
print(result)
#
# while True:
#     try:
#         s = input('calc > ')
#     except EOFError:
#         break
#     if not s: continue
#     result = parser.parse(s)
#     print(result)
#