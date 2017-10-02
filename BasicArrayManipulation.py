import random


class ArrayClass:

    def __init__(self):

        self.array_size = 10
        self.the_array = [None] * self.array_size

    def generate_random_array(self):

        for values in range(self.array_size):

            self.the_array[values] = random.randrange(10, 20)

    def print_array(self):

        print("----------")
        for i in range(self.array_size):
            print("| " + str(i) + " | " + str(self.the_array[i]) + " |" + "\n----------")

    def get_value_at_index(self, index):

        if index < self.array_size:
            return self.the_array[index]
        return 0

    def linear_search(self, item):

        value_in_array = False
        index_with_value = ""

        print("The value was found in the following index(s)")

        for i in range(self.array_size):

            if self.the_array[i] == item:
                value_in_array = True
                index_with_value += str(i) + " "

        if not value_in_array:
            index_with_value = "None"

        return index_with_value

    def swap_values(self, index_one, index_two):

        temp = self.the_array[index_one]
        self.the_array[index_one] = self.the_array[index_two]
        self.the_array[index_two] = temp

array = ArrayClass()

array.generate_random_array()
array.print_array()
print(array.get_value_at_index(1))
print(array.linear_search(12))
