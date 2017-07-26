def sequential_search(list_items, item):

    pos = 0
    found = False

    while pos < len(list_items) and not found:

        if list_items[pos] == item:
            found = True
            print(list_items[pos], item)
        else:
            pos += 1
    return found

list1 = [1, 2, 4, 5, 6, 7, 8]

print(sequential_search(list1, 4))
