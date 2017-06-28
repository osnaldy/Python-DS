import random
import timeit


for i in range(10000, 1000001, 20000):

    # set dictionary to verify that is it O(1)
    set_dict = timeit.Timer("x[random.randrange(%d)]" % i, "from __main__ import random, x")

    # get dictionary to verify that is it O(1)
    get_dict = timeit.Timer("x.get(random.randrange(%d))" % i, "from __main__ import random, x")
    x = {j: None for j in range(i)}

    dict_set = set_dict.timeit(number=1000)
    dict_get = get_dict.timeit(number=1000)

    print ("%d,%10.4f,%10.4f" % (i, dict_set, dict_get))
