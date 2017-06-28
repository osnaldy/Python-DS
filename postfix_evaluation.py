from Stack import Stack


def postfix_eval(postfix_exp):

    operand_stack = Stack()

    postfix_list = postfix_exp.split()

    for token in postfix_list:

        if token in '1234567890':

            token = int(token)

            operand_stack.push(token)

        else:

            operand2 = operand_stack.pop()

            operand1 = operand_stack.pop()

            result = do_math(token, operand1, operand2)

            operand_stack.push(result)

    return operand_stack.pop()


def do_math(op, op1, op2):

    if op == '*':

        return op1 * op2

    elif op == '/':

        return op1 / op2

    elif op == '+':

        return op1 + op2

    else:

        return op1 - op2

print(postfix_eval(' 7 8 + 3 2 + / '))
