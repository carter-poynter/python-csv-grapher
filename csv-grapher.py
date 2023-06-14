import turtle
import csv

def plot_data_points(file_path):
    # Open the CSV file
    with open(file_path, 'r') as file:
        # Read the CSV data
        data = list(csv.reader(file))

        scaleFactor = 30

        # Initialize the turtle at the first data point
        first_row = data[0]
        turtle.Screen().bgcolor("#1E1E1E")
        turtle.hideturtle()
        turtle.penup()
        turtle.goto(int(first_row[0]) * scaleFactor - 450, int(first_row[1]) * scaleFactor / 15 - 100)
        turtle.pendown()

        # Set up turtle graphics
        turtle.speed(0)
        turtle.width(3)

        # Iterate over the data and plot the points
        previous_x = int(first_row[0]) * scaleFactor
        previous_y = int(first_row[1]) * scaleFactor / 15
        for row in data[1:]:
            # Extract the x and y coordinates from each row
            x = int(row[0]) * scaleFactor
            y = int(row[1]) * scaleFactor / 15

            # Set the line color based on the trend
            if y > previous_y:
                turtle.pencolor('green')
            elif y < previous_y:
                turtle.pencolor('red')

            turtle.goto(x - 450, y - 100)

            previous_x = x
            previous_y = y

        # Go back to the beginning and plot black data points
        turtle.pencolor('white')
        turtle.penup()
        turtle.goto(int(first_row[0]) * scaleFactor - 450, int(first_row[1]) * scaleFactor / 15 - 100)
        for row in data[1:]:
            x = int(row[0]) * scaleFactor
            y = int(row[1]) * scaleFactor / 15
            turtle.goto(x - 450, y - 100)
            turtle.dot(6)  # Plot a black data point

        turtle.penup()
        turtle.goto(-450, -100)

        num_rows = len(data)

        for i in range(num_rows):
            turtle.setheading(0)
            turtle.pendown()
            turtle.forward(scaleFactor)
            turtle.setheading(90)
            turtle.forward(10)
            turtle.setheading(270)
            turtle.forward(20)
            turtle.penup()
            turtle.forward(20)
            turtle.write(i + 1, align="center")
            turtle.setheading(90)
            turtle.forward(20)
            turtle.forward(10)

        turtle.goto(-450, -100)

        for i in range(20):
            turtle.setheading(90)
            turtle.pendown()
            turtle.forward(20)
            turtle.setheading(180)
            turtle.forward(10)
            turtle.setheading(0)
            turtle.forward(20)
            turtle.penup()
            turtle.forward(20)
            turtle.setheading(180)
            turtle.forward(30)
            turtle.forward(20)
            turtle.write((i + 1) * 10, align="center")
            turtle.forward(-20)

        # Exit the turtle graphics window on click
        turtle.exitonclick()

# Provide the path to your CSV file
csv_file_path = 'stockIndex.csv'

# Call the function to plot the data points
plot_data_points(csv_file_path)
