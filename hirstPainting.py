# Import the turtle graphics library and the random module
import turtle
import random

# Define a function to generate a random RGB color
def random_color():
    return (random.randint(0, 255) ,random.randint(0, 255) ,random.randint(0, 255))

# Create a turtle object named 'dots'
dots = turtle.Turtle()

# Lift the pen to prevent drawing while positioning
dots.penup()

# Set the background color to black
turtle.bgcolor("black")

# Set the color mode to 255 (RGB)
turtle.colormode(255)

# Hide the turtle cursor
dots.hideturtle()

# Set the drawing speed to maximum
dots.speed(0)

# Set initial coordinates for drawing
y = -230.0
x = -230.0

# Loop to draw rows of dots
for _ in range(10):
    dots.goto(x,y)
    # Loop to draw a row of dots
    for _ in range (10):
        dots.dot(20 , random_color())  # Draw a dot with random color
        dots.forward(50)  # Move the turtle forward for the next dot in the row
    y += 50  # Move the turtle down for the next row

# Create a screen object
screen = turtle.Screen()

# Exit the program when the screen is clicked
screen.exitonclick()
