ones = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen",
        "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]

tens = ["Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]


def convert_integer_to_string(n):

    word = ""

    if n == 0:

        word = "Zero"

    elif n <= 19:

        word += ones[n - 1]

    elif n <= 99:

        word += tens[n // 10 - 2]
        n = n % 10

        if n != 0:

            word += " " + ones[n - 1]

        else:

            word += ""

    elif n <= 999:

        word += ones[n // 100 - 1] + " Hundred "
        n = n % 100

        if n == 0:

            word += ""

        elif n <= 19:

            word += ones[n - 1]

        elif n <= 99:

            word += tens[n // 10 - 2] + " "
            n = n % 10

            if n != 0:

                word += ones[n-1]

            else:

                word += ""

    return word

print(convert_integer_to_string(23))
