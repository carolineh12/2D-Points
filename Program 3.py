########################################################################################################
# 2D Points
# Liz Denson & Caroline Holland
# Last modified on 2023-02-28
#
# An object-oriented program that utilizes a GUI and includes a 2D Point class instantiating randomly
# generated points within a specified coordinate range, and plotting those points on a canvas.
########################################################################################################

# Import libraries
from tkinter import *
from random import randint, choice
import math

# Point class
class Point:
    # Constructor that initializes a Point with specified values for x and y
    # Defaults the 0.0 value for both components
    def __init__(self, x=0.0, y=0.0):
        # Instance variables where each component is a floating point value
        self._x = float(x)
        self._y = float(y)
    
    # Getters
    def get_x(self):
        # Accessor for the x component
        return self._x
    
    def get_y(self):
        # Accessor for the y component
        return self._y
    
    # Setters
    def set_x(self, value):
        # Mutator method for the x component
        self._x = float(value)
        
    def set_y(self, value):
        # Mutator method for the y component
        self._y = float(value)
        
    # Call x and y getters and setters through the property function
    x = property(get_x, set_x)
    y = property(get_y, set_y)
    
    # Calculate the distance between two points and takes another point as an argument
    def dist(self, other_point):
        # Distance formula to calculate the distance between the two points
        return math.sqrt((self._x - other_point.get_x()) ** 2 +
                         (self._y - other_point.get_y()) ** 2)

    # Calculate the midpoint between two points and takes another point as an argument
    def midpt(self, other_point):
        # Calculates the average of the x and y components of the two points
        mid_x = (self._x + other_point.get_x()) / 2.0
        mid_y = (self._y + other_point.get_y()) / 2.0
        # Returns a new point instance with the midpoint coordinates
        return Point(mid_x, mid_y)

    # Magic method to provide a string representation of the point instance
    def __str__(self):
        # Returns a string in the format (x,y)
        return "({}, {})".format(self._x, self._y)

# CoordinateSystem class varaibles
# Class variable that sets the width to 800
WIDTH = 800
# Class variable that sets the height to 800
HEIGHT = 800
# Class variable for the possible colors of the plotted points
POINT_COLORS = ['black', 'red', 'green', 'blue', 'cyan', 'yellow', 'magenta']
# Class variable for the radius of the plotted points
POINT_RADIUS = 0
# Class variable that sets the number of points to 5000
NUM_POINTS = 5000

# The CoordinateSystem class inheriting from Tkinter's Canvas class
class CoordinateSystem(Canvas):
    # Constructor for the CoordinateSystem class
    def __init__(self, master, width=WIDTH, height=HEIGHT, num_points=NUM_POINTS):
        # Initialize a canvas object with the width, height, and white background
        super().__init__(master, width=width, height=height, bg='white')
        # Pack the canvas object to fill the entire Tkinter window
        self.pack(fill=BOTH, expand=True)
        # Instance variable for the number of points to plot
        self.num_points = num_points

    # Method to plot a single point on the canvas
    def plot(self, p):
        # Get the x and y coordinates of the point
        x = p.get_x()
        y = p.get_y()
        
        #Pick random color to fill point
        color = choice(POINT_COLORS)

        # Create an oval with a radius of POINT_RADIUS centered
        # on the point's x and y coordinates with the specified color
        self.create_oval(x, y, x + POINT_RADIUS, y + POINT_RADIUS, outline=color, fill=color)

    # Method to plot multiple random points on the canvas
    def plotPoints(self, n):
        # Plot n random points on the canvas within the specified width and height
        for i in range(n):
            x = randint(0, WIDTH - 1)
            y = randint(0, HEIGHT - 1)
            p = Point(x, y)
            self.plot(p)
    

###############
# MAIN PROGRAM
###############

# Create a Tkinter window
window = Tk()
# Set the geometry of the window to the specified WIDTH and HEIGHT
window.geometry("{}x{}".format(WIDTH, HEIGHT))
# Set the title of the window
window.title("Points can be fun!")
# Create an instance of the CoordinateSystem class on the Tkinter window
p = CoordinateSystem(window)
# Call the plotPoints() method to plot NUM_POINTS random points on the canvas
p.plotPoints(NUM_POINTS)
# Start the Tkinter event loop
window.mainloop()