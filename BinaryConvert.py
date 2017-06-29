from Stack import Stack


def divide_by_2(dec_number):

    rem_stack = Stack()

    while dec_number > 0:

        rem = dec_number % 2

        rem_stack.push(rem)

        dec_number //= 2

    binary_string = ''

    while not rem_stack.is_empty():

        binary_string = binary_string + str(rem_stack.pop())

    return binary_string

print(divide_by_2(20))
