def move(n, start, destination, helper):

    if n > 1:

        move(n - 1, start, helper, destination)

        move(1, start, destination, helper)

        move(n - 1, helper, destination, start)

    else:

        print(start, "-->", destination)


def hanoi(h):

    move(h, "1", "3", "2")

hanoi(3)
