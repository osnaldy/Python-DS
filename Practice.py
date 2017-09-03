num_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]

for index in range(1, len(num_list)):

    current_value = num_list[index]
    position = index

    while position > 0 and num_list[position - 1] > current_value:

        num_list[position] = num_list[position - 1]
        position -= 1

    num_list[position] = current_value
print(num_list)
