def binary_search_recursively(list_items, item):

    if len(list_items) == 0:

        return False

    else:

        midpoint = len(list_items) // 2

    if list_items[midpoint] == item:

        return True

    else:

        if item < list_items[midpoint]:

            return binary_search_recursively(list_items[:midpoint], item)

        else:

            return binary_search_recursively(list_items[midpoint + 1:], item)

lists = [1, 2, 4, 5, 10, 23, 34, 44]
print(binary_search_recursively(lists, 22))
