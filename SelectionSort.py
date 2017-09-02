def selection_sort(a_list):

    for fill_slots in range(len(a_list) - 1, 0, - 1):

        max_index = 0

        for i in range(1, fill_slots + 1):

            if a_list[i] > a_list[max_index]:

                max_index = i

        temp = a_list[fill_slots]
        a_list[fill_slots] = a_list[max_index]
        a_list[max_index] = temp

num = [54, 26, 93, 17, 77, 31, 44, 55, 20]
selection_sort(num)
print(num)


# Another way to approach this problem of Selection Sort, is by finding the minimum
def selection_sort_algorithm(a_list):

    for i in range(len(a_list)):

        min_index = i

        for j in range(i + 1, len(a_list)):

            if a_list[min_index] > a_list[j]:

                min_index = j
        a_list[i], a_list[min_index] = a_list[min_index], a_list[i]

num1 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
selection_sort_algorithm(num1)
print(num1)
