"""This module uses recursion to create the "Koch snowflake" fractal"""

import turtle


def koch_snowflake(t, order, size):
    """Function recursively calculates each segment of the fractal"""
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_snowflake(t, order - 1, size / 3)
            t.left(angle)


def main():
    """Prompt user for the recursion level"""
    recursion_level = int(input("Enter the recursion level: "))

    # Setup turtle
    screen = turtle.Screen()
    screen.setup(width=800, height=800)
    screen.bgcolor("white")
    screen.title("Koch Snowflake")

    t = turtle.Turtle()
    t.speed(0)  # Set the speed of the turtle (0 is the fastest)

    # Positioning the turtle
    t.penup()
    t.goto(-150, 90)
    t.pendown()

    # Draw the snowflake
    for i in range(3):
        koch_snowflake(t, recursion_level, 300)
        t.right(120)

    # Hide the turtle
    t.hideturtle()

    # Keep the window open
    screen.mainloop()


if __name__ == "__main__":
    main()
