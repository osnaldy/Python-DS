from Stack import Stack


def parenthesis_checker(symbol_string):

    s = Stack()

    for i in range(len(symbol_string)):

        symbol = symbol_string[i]

        if symbol == "(":

            s.push(symbol)

        else:

            if s.is_empty():

                return False

            else:

                s.pop()

        i += 1

    if True and s.is_empty():

        return True
    else:
        return False

print(parenthesis_checker('(())()'))


def matches(open, close):

    opens = '([{'
    closes = ')]}'

    return opens.index(open) == closes.index(close)


def symbol_checker(symbol_string):

    s = Stack()

    for i in range(len(symbol_string)):

        symbol = symbol_string[i]

        if symbol in '([{':

            s.push(symbol)

        else:

            if s.is_empty():

                return False

            else:

                top = s.pop()

                if not matches(top, symbol):

                    return False
        i += 1

    if True and s.is_empty():

        return True

    else:

        return False

print(symbol_checker('{{([][])}()}'))
print(symbol_checker('[{()]'))
