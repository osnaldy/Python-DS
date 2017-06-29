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

print(infix_to_postfix(" ( B * B ) + ( C + D ) "))
print(infix_to_postfix("5 * 3 ^ ( 4 - 2 )"))
