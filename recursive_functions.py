# -----------Created a function to add recursively -----------------
def list_sum(num_list):

    if len(num_list) == 1:
        return num_list[0]
    else:
        return num_list[0] + list_sum(num_list[1:])

print(list_sum([1, 4, 5, 2, 3]), "is the sum of all the numbers")


# -----------Created a function to convert integer to string of any base -----------------
def to_string(n, base):

    convert_string = "0123456789ABCDEF"

    if n < base:
        return convert_string[n]
    else:
        return to_string(n // base, base) + convert_string[n % base]

print(to_string(10, 2))


# -----------Created a function to add recursively -----------------
def reverse_string(string):

    if len(string) == 1:
        return string
    else:
        return reverse_string(string[1:]) + string[0]

print(reverse_string('Hello World'))


def check_palindrome(string):
    # remove all the white spaces and punctuation from string
    new_string = ''.join(n.lower() for n in string if n.isalnum())

    if len(new_string) <= 1:
        return True
    else:
        if new_string[0] != new_string[-1]:
            return False
        else:
            return check_palindrome(new_string[1: -1])

print(check_palindrome('kayak'))
print(check_palindrome('aibohphobia'))
print(check_palindrome('Reviled did I live, said I, as evil I did deliver'))
print(check_palindrome('Able was I ere I saw Elba'))
print(check_palindrome('Kanakanak – a town in Alaska'))
print(check_palindrome('Wassamassaw – a town in South Dakota'))
