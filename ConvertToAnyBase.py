from Stack import Stack


def base_converter(dec_number, base):
    digits = '0123456789ABCDEF'

    stack = Stack()

    while dec_number > 0:

        rem = dec_number % base

        stack.push(rem)

        dec_number //= base

    new_string = ""

    while not stack.is_empty():

        new_string += digits[stack.pop()]

    return new_string

print(base_converter(42, 2))

print(base_converter(26, 16))
