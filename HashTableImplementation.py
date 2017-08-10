class HashTable:

    def __init__(self):
        self.size = 11
        # creates an array to hold the index of each slot
        self.slots = [None] * self.size
        # create an array to hold data, which will be parallel to the indez
        self.data = [None] * self.size

    @staticmethod
    def hash_function(key, size):

        return key % size

    @staticmethod
    def rehash(old_hash, size):

        return (old_hash + 1) % size

    # Class method to insert data into the slots
    def put(self, key, data):

        # compute the original hash value to then compare
        hash_value = self.hash_function(key, len(self.slots))

        # check if the slot/bucket is None(empty), if so, it will assign an index and data to slot
        if self.slots[hash_value] is None:
            self.slots[hash_value] = key
            self.data[hash_value] = data
        else:
            if self.slots[hash_value] == key:
                # if the key exists, it replaces the data with the new given data
                self.data[hash_value] = data
            # now we will check if we need to rehash and find another slot for the given key
            else:
                next_slot = self.rehash(hash_value, len(self.slots))

                # it will loop until it finds the next empty
                while self.slots[next_slot] is not None and self.slots[next_slot] != key:
                    next_slot = self.rehash(next_slot, len(self.slots))

                if self.slots[next_slot] is None:
                    self.slots[next_slot] = key
                    self.data[next_slot] = data

                else:
                    self.slots[next_slot] = data

    def get(self, key):

        start_slot = self.hash_function(key, len(self.slots))

        data = None
        stop = False
        found = False
        position = start_slot

        while self.slots[position] is not None and not found and not stop:

            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots))
                if position == start_slot:
                    stop = True
        return data

    def __len__(self):

        return len([x for x in self.slots if x])

    def __getitem__(self, key):

        return self.get(key)

    def __setitem__(self, key, data):

        self.put(key, data)
