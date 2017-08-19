def selection_sort(a_list):

    for fill_slot in range(len(a_list) - 1, 0, - 1):

        max_index = 0

        for location in range(1, fill_slot + 1):

            if a_list[location] > a_list[max_index]:

                max_index = location

        temp = a_list[fill_slot]
        a_list[fill_slot] = a_list[max_index]
        a_list[max_index] = temp

num = [54, 26, 93, 17, 77, 31, 44, 55, 20]
selection_sort(num)
print(num)
