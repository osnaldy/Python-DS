def binary_search(list_items, item):

    first = 0
    last = len(list_items) - 1
    found = False

    while first <= last and not found:

        midpoint = (first + last) // 2

        if list_items[midpoint] == item:

            found = True

        else:

            if item < list_items[midpoint]:

                last = midpoint - 1

            else:

                first = midpoint + 1

    return found

lists = [1, 2, 4, 5, 10, 23, 34, 44]
print(binary_search(lists, 11))
