from MainDeque import Deque


def palindrome_checker(a_string):

    char_check = Deque()

    for ch in a_string:

        char_check.add_rear(ch)

    while char_check.size() > 1 and True:

        first = char_check.remove_front()
        last = char_check.remove_rear()

        if first != last:

            return False

        else:

            return True

print(palindrome_checker('radar'))
print(palindrome_checker('root'))
print(palindrome_checker('madam'))
