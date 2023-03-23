########################################################################################################
# Chaos Game
# Liz Denson & Caroline Holland
# Last modified on 2023-03-23
#
# An object-oriented program that utilizes a GUI to create the Chaos Game.
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
        
    # Calls x and y getters and setters through the property function
    x = property(get_x, set_x)
    y = property(get_y, set_y)
    
    # Calculates the distance between two points and takes another point as an argument
    def dist(self, other_point):
        # Distance formula that calculates the distance between the two points
        return math.sqrt((self._x - other_point.get_x()) ** 2 +
                         (self._y - other_point.get_y()) ** 2)

    # Calculates the midpoint between two points and takes another point as an argument
    def midpt(self, other_point):
        # Calculates the average of the x and y components of the two points
        mid_x = (self._x + other_point.get_x()) / 2.0
        mid_y = (self._y + other_point.get_y()) / 2.0
        # Returns a new point instance with the midpoint coordinates
        return Point(mid_x, mid_y)

    # Magic method that provides a string representation of the point instance
    def __str__(self):
        # Returns a string in the format (x,y)
        return "({}, {})".format(self._x, self._y)

# Constants for the ChaosGame class
# The dimensions of the canvas and the number of points to be plotted
WIDTH = 600
HEIGHT = 520
NUM_POINTS = 50000
# The minimum and maximum values for X and Y coordinates
MIN_X = 0
MAX_X = WIDTH - 1
MIN_Y = 0
MAX_Y = HEIGHT - 1
# The midpoint values for X and Y coordinates
MID_X = (MIN_X + MAX_X) / 2
MID_Y = (MIN_Y + MAX_Y) / 2
# The colors and radius sizes for the points and vertices
POINT_COLOR = ['black']
VERTEX_COLOR = ['red']
POINT_RADIUS = 0
VERTEX_RADIUS = 3

# ChaosGame class
class ChaosGame(Canvas):
    # Constructor for the ChaosGame class
    def __init__(self, master, width=WIDTH, height=HEIGHT, num_points=NUM_POINTS):
        # Initializes a canvas with the width, height, and a white background
        super().__init__(master, width=width, height=height, bg='white')
        # Pack the canvas to fill the entire Tkinter window
        self.pack(fill=BOTH, expand=True)
        # Instance variable for the number of points to plot
        self.num_points = num_points

    # Method to plot a single point with specified color and radius
    def plot(self, p, color, radius):
        # Get the X and Y coordinates of a point and plot them
        x = p.get_x()
        y = p.get_y()
        self.create_oval(x, y, x + radius, y + radius, outline=color, fill=color)

    # Method to plot multiple midpoints
    def plotMidpoints(self, vertices, max_points):
        count = 1
        # Choose a random vertex to be the starting point
        m = choice(vertices)
        # Continue plotting midpoints until the maximum number of points has been reached
        while count < max_points:
            v = choice(vertices)
            m_new = m.midpt(v)
            self.plot(m_new, POINT_COLOR, POINT_RADIUS)
            m = m_new
            count += 1

    # Method to plot the vertices of the triangle
    def plotTriangle(self, vertices):
        for vertex in vertices:
            self.plot(vertex, VERTEX_COLOR, VERTEX_RADIUS)

###############
# MAIN PROGRAM
###############

# Function to create an equilateral triangle given a side length and center coordinates
def sierpinskiTriangle(base_length, x_center, y_center):
    height = base_length * (math.sqrt(3) / 2)
    v1 = Point(x_center, y_center - (height / 2))
    v2 = Point(x_center - (base_length / 2), y_center + (height / 2))
    v3 = Point(x_center + (base_length / 2), y_center + (height / 2))
    return [v1, v2, v3]

# Creates the main application window
window = Tk()
# Sets the size of the window
window.geometry("{}x{}".format(WIDTH, HEIGHT))
# Sets the title of the window
window.title("Chaos Game!")
# Creates an instance of the ChaosGame class
p = ChaosGame(window)
# Generates the vertices of the equilateral triangle
triangle_vertices = sierpinskiTriangle(584, MID_X, MID_Y)
# Plots the vertices of the triangle
p.plotTriangle(triangle_vertices)
# Plots the midpoints
p.plotMidpoints(triangle_vertices, NUM_POINTS)
# Runs the main event loop
window.mainloop()
