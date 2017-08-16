def short_bubble_sort(a_list):

    exchange = True

    pass_number = len(a_list) - 1

    while pass_number > 0 and exchange:

        exchange = False

        for i in range(pass_number):

            if a_list[i] > a_list[i + 1]:

                exchange = True
                temp = a_list[i]
                a_list[i] = a_list[i + 1]
                a_list[i + 1] = temp
        pass_number -= 1

list_number = [5, 2, 7, 3, 6, 1, 4]

short_bubble_sort(list_number)

print(list_number)