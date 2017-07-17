from Stack import Stack


def infix_to_postfix(infix_exp):

    precedence = {}

    precedence['^'] = 4
    precedence['*'] = 3
    precedence['/'] = 3
    precedence['+'] = 2
    precedence['-'] = 2
    precedence['('] = 1

    op_stack = Stack()

    postfix_list = []

    token_list = infix_exp.split()

    for token in token_list:

        if token in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' or token in '1234567890':

            postfix_list.append(token)

        elif token == '(':

            op_stack.push(token)

        elif token == ')':

            top_token = op_stack.pop()

            while top_token != '(':

                postfix_list.append(top_token)
                top_token = op_stack.pop()

        else:

            while (not op_stack.is_empty()) and (precedence[op_stack.peek()] >= precedence[token]):

                postfix_list.append(op_stack.pop())
            op_stack.push(token)

    while not op_stack.is_empty():

        postfix_list.append(op_stack.pop())

    return ' '.join(postfix_list)


def balance_check(symbol_string):

    s = Stack()

    for i in range(len(symbol_string)):

        symbol = symbol_string[i]

        if symbol == '(':

            s.push(symbol)

        else:

            if s.is_empty():
                return False

            else:
                s.pop()
        i += 1

    if s.is_empty():
        return True
    else:
        return False


def validate_infix_expression(expr):

    if not expr:
        return False

    expressions = []

    for i in range(len(expr)):
        if expr[i] == '(' or expr[i] == ')':
            expressions.append(expr[i])
    if not balance_check(expressions):
        return False
    else:
        return True
expression = " ( B * B ) + ( C + D ) "
token = validate_infix_expression(expression)

if token is True:

    print(infix_to_postfix(expression))

else:

    print("Incorrect input")

print(infix_to_postfix("5 * 3 ^ ( 4 - 2 )"))