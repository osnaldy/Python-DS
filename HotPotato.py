from MainQueue import Queue
import random


def hot_potato(name_list, num):

    queue = Queue()

    for name in name_list:

        queue.enqueue(name)

    while queue.size() > 1:

        for i in range(random.randrange(num)):

            queue.enqueue(queue.dequeue())

        queue.dequeue()

    return queue.dequeue()

name_list = ['Derian', 'Osnaldy', 'Andy', 'Osneily', 'Ainara', 'Lucia']

print(hot_potato(name_list, 7))

