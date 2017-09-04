# Find the number in a given array
# HackerRank Challenge


def num_search(arr, k):

    y = ""
    for i in range(len(arr)):

        if arr[i] == k:
            y = "YES"

        elif arr[i] != k:
            y = "NO"
    return y

num = [1, 2, 4, 5, 4, 6, 7]
print(num_search(num, 8))

# Return the odd numbers from an Array
# HackerRank Challenge


def find_odd(s, r):

    while s <= r:

        if s % 2 != 0:
            print(s)
        s += 1

l = 2
j = 5

find_odd(l, j)

# Game that find who is the winner between two players using the Odd or Even index of an array
# HackerRank Challenge


def find_winner(andrea, maria, s):

    count_a = 0
    count_m = 0
    a = ""

    if s == "Even":
        a = andrea[::2]
        m = maria[::2]
        print(a)
        print(m)

        for i, j in zip(a, m):

            count_a += i - j
            count_m += j - i

        if count_a > count_m:
            a = "Andrea"
        elif count_m > count_a:
            a = "Maria"
        else:
            a = "Tie"

    elif s == "Odd":
        a = andrea[1::2]
        m = maria[1::2]
        print(a)
        print(m)

        for i, j in zip(a, m):
            count_a += i - j
            count_m += j - i

        if count_a > count_m:
            a = "Andrea"
        elif count_m > count_a:
            a = "Maria"
        else:
            a = "Tie"
    return a

andr = [1, 3, 4, 1, 1, 2, 1]
mar = [7, 6, 3, 6, 1, 7, 2]

print(find_winner(andr, mar, "Odd"))
