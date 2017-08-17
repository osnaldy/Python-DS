def selection_sort_algorithm(a_list):

    for i in range(len(a_list) - 1, 0, - 1):

        pos_of_max = 0

        for j in range(1, i + 1):

            if a_list[j] > a_list[pos_of_max]:

                pos_of_max = j
        temp = a_list[i]
        a_list[i] = a_list[pos_of_max]
        a_list[pos_of_max] = temp

a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
selection_sort_algorithm(a_list)
print(a_list)