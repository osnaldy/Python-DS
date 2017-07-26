def order_sequence(items_list, item):

    pos = 0
    stop = False
    found = False

    while pos < len(items_list) and not found and not stop:

        if items_list[pos] == item:
            found = True

        else:

            if items_list[pos] > item:
                stop = True

            else:
                print(str(items_list[pos]) + " does not equal " + str(item))
                pos += 1

    return found

list1 = [1, 2, 33, 44, 5]

print(order_sequence(list1, 37))
