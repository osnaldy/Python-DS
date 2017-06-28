import random
import timeit

# through this example I was able to confirm that the index operation is O(1).

for i in range(10000, 1000001, 20000):

    t = timeit.Timer("x[(random.randrange(%d))]" % i, "from __main__ import random, x")

    x = list(range(i))

    list_indexing = t.timeit(number=1000)

    print("%d,%10.3f" % (i, list_indexing))


