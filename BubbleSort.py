def bubble_sort(a_list):

    for pass_number in range(len(a_list) - 1, 0, -1):

        for i in range(pass_number):

            if a_list[i] > a_list[i + 1]:
                temp = a_list[i]
                a_list[i] = a_list[i + 1]
                a_list[i + 1] = temp

number = [10, 3, 1, 8, 2, 7, 5]

bubble_sort(number)

print(number)
