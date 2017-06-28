import timeit
import random

for i in range(10000, 100001, 20000):

    t = timeit.Timer("del next(xiter)[random.randrange(%d)]" % i, "from __main__ import random, xiter")

    x = [list(range(i)) for _ in range(1000)]
    xiter = iter(x)
    delListTime = t.timeit(number=1000)

    x = [dict.fromkeys(range(i)) for _ in range(1000)]
    xiter = iter(x)

    delDictTime = t.timeit(number=1000)

    print("%d,%10.4f,%10.4f" % (i, delDictTime, delListTime))
