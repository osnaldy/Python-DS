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

