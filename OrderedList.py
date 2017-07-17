from MainNode import Node


class OrderedList:

    def __init__(self):

        self.head = None

    def is_empty(self):

        return self.head is None

    def size(self):

        size = self.is_empty()
        if size is None:
            return

        current = self.head
        count = 0

        while current is not None:
            count += 1
            current = current.next
        return count

    def remove(self, item):

        current = self.head
        prev = None
        found = False

        while not found:

            if current.get_data() != item:
                return str(item) + " Not found"

            if current.get_data() == item:
                found = True
            else:
                prev = current
                current = current.next

        if prev is None:
            self.head = current.next
        else:
            prev.set_next(current.get_next())

        return current.get_data()

    def search(self, item):

        current = self.head
        stop = False
        found = False

        while current is not None and not found and not stop:

            if current.get_data() == item:
                found = True
            else:
                if current.get_data() > item:
                    stop = True
                else:
                    current = current.next

        return found

    def add(self, item):

        current = self.head
        prev = None
        stop = False

        while current is not None and not stop:

            if current.get_data() > item:
                stop = True

            else:
                prev = current
                current = current.get_next()

        temp = Node(item)

        if prev is None:
            temp.set_next(self.head)
            self.head = temp
        else:
            temp.set_next(current)
            prev.set_next(temp)

    def print_list(self):

        current = self.head

        while current is not None:

            print (current.get_data(), "-->", end=' ')
            current = current.get_next()

myList = OrderedList()
myList.add(23)
myList.add(77)
myList.add(44)
myList.add(5)

print(myList.print_list())
