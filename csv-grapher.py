import turtle
import csv

def plot_data_points(file_path):
    # Open the CSV file
    with open(file_path, 'r') as file:
        # Read the CSV data
        data = csv.reader(file)

        # Initialize the turtle
        turtle.speed(0)
        turtle.penup()
        turtle.width(3)

        # Iterate over the data and plot the points
        previous_x = None
        previous_y = None
        for i, row in enumerate(data):
            # Extract the x and y coordinates from each row
            x = int(row[0]) * 10
            y = int(row[1])

            # Set the line color based on the trend
            if previous_y is not None:
                if y > previous_y:
                    turtle.goto(x, y)
                    turtle.pencolor('green')
                    turtle.pendown()
                elif y < previous_y:                    
                    turtle.goto(x, y)
                    turtle.pencolor('red')
                    turtle.pendown()

            previous_x = x
            previous_y = y

        # Exit the turtle graphics window on click
        turtle.exitonclick()

# Provide the path to your CSV file
csv_file_path = 'stockIndex.csv'

# Call the function to plot the data points
plot_data_points(csv_file_path)