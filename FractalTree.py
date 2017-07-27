import turtle


def tree(branch_len, t):
    if branch_len > 5:
        t.forward(branch_len)
        t.right(30)
        tree(branch_len - 15, t)
        t.left(60)
        tree(branch_len - 15, t)
        t.right(30)
        t.backward(branch_len)


def main():

    t = turtle.Turtle()
    my_win = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("black")
    tree(85, t)
    my_win.exitonclick()

main()