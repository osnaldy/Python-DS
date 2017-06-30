import time


def sums(n):

    start = time.time()
    the_sum = 0

    for i in range(1, n+1):

        the_sum += i

    end = time.time()
    return the_sum, end-start

for i in range(5):
    print("sum is %d and required %f seconds" % sums(1000000))
