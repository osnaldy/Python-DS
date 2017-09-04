# Find the number in a given function
# Hackerrank challenge


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

