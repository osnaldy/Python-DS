import random


class ArrayClass:

    def __init__(self):

        self.array_size = 10
        self.the_array = [None] * 50

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

    def insert_value_at_the_end_of_array(self, value):

        if self.array_size < 50:

            self.the_array[self.array_size] = value

            self.array_size += 1

    def delete_index(self, index):

        if index < self.array_size:

            for i in range(index, self.array_size - 1):

                self.the_array[i] = self.the_array[i + 1]

            self.array_size -= 1

    def bubble_sort(self):

        for i in range(0, self.array_size - 1):

            for j in range(0, self.array_size - 1 - i):

                if self.the_array[j] > self.the_array[j + 1]:

                    self.swap_values(j, j+1)

    def swap_values(self, index_one, index_two):

        temp = self.the_array[index_one]
        self.the_array[index_one] = self.the_array[index_two]
        self.the_array[index_two] = temp

array = ArrayClass()

array.generate_random_array()
array.insert_value_at_the_end_of_array(24)
array.delete_index(3)
array.bubble_sort()
array.print_array()
print(array.get_value_at_index(1))
print(array.linear_search(12))
