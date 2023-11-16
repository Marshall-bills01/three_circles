import turtle

# Create a new turtle screen and set its background color
screen = turtle.Screen()
screen.bgcolor("white")

# Create a new turtle object
circle = turtle.Turtle()

# Define the radius and colors for the circles
radii = [50, 100, 150]
colors = ["red", "green", "blue"]

# Draw the circles
for radius, color in zip(radii, colors):
    circle.fillcolor(color)
    circle.begin_fill()
    circle.circle(radius)
    circle.end_fill()
    circle.penup()
    circle.goto(0, -radius-50)  # Move the turtle down
    circle.pendown()

# Hide the turtle and close the turtle graphics window
circle.hideturtle()
turtle.done()
