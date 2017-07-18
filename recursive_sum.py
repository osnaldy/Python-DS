def list_sum(num_list):

    if len(num_list) == 1:
        return num_list[0]
    else:
        return num_list[0] + list_sum(num_list[1:])

print(list_sum([1, 4, 5, 2, 3]), "is the sum of all the numbers")


def to_string(n, base):

    convert_string = "0123456789ABCDEF"

    if n < base:
        return convert_string[n]
    else:
        return to_string(n // base, base) + convert_string[n % base]

print(to_string(42, 2))
