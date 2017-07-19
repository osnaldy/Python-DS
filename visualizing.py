import turtle

my_turtle = turtle.Turtle()
my_turtle.shape("turtle")

my_win = turtle.Screen()


def draw_spiral(my_turtle, line_len):

    # Forward moves in pixels
    # Left and right moves in degrees

    if line_len > 0:
        my_turtle.forward(line_len)
        my_turtle.left(90)
        draw_spiral(my_turtle, line_len - 5)

draw_spiral(my_turtle, 100)
my_win.exitonclick()
