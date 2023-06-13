import turtle
import csv

def plot_data_points(file_path):
    # Open the CSV file
    with open(file_path, 'r') as file:
        # Read the CSV data
        data = csv.reader(file)

        # Initialize the turtle at the first data point
        first_row = next(data)
        turtle.penup()
        turtle.goto(int(first_row[0]) * 20 - 300, int(first_row[1]) * 2)
        turtle.pendown()

        # Set up turtle graphics
        turtle.speed(0)
        turtle.width(3)

        # Iterate over the data and plot the points
        previous_x = int(first_row[0]) * 20
        previous_y = int(first_row[1]) * 2
        for row in data:
            # Extract the x and y coordinates from each row
            x = int(row[0]) * 20
            y = int(row[1]) * 2

            # Set the line color based on the trend
            if y > previous_y:
                turtle.pencolor('green')
            elif y < previous_y:
                turtle.pencolor('red')

            turtle.goto(x - 300 , y)

            previous_x = x
            previous_y = y

        # Go back to the beginning and plot black data points
        turtle.pencolor('black')
        turtle.penup()
        file.seek(0)  # Reset the file pointer
        for row in data:
            x = int(row[0]) * 20
            y = int(row[1]) * 2
            turtle.goto(x - 300, y)
            turtle.dot(8)  # Plot a black data point

        # Exit the turtle graphics window on click
        turtle.exitonclick()

# Provide the path to your CSV file
csv_file_path = 'stockIndex.csv'

# Call the function to plot the data points
plot_data_points(csv_file_path)