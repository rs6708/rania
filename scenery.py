#The following python turtle code task below will go step by step with the docstrings explaining each 
# function in order, to draw a table with 4 legs and a birthday cake with 3 layers. Taking users input 
# for the width, color of the table, adding balloons as the decoration, a candle, and a happy birthday 
# text.


#Jad's github repository link: https://github.com/jk4201-code/jads-repository
#khalifa's github repository link: https://github.com/kaa8006/khalifa-repository.git
#rania's github repository link: https://github.com/rs6708/rania.git

import turtle

# Function to draw a rectangle (reusable for table and legs)
def draw_rectangle(length, width, color):
    """
    Draws a rectangle of specified length, width, and color.
    
    Parameters:
        length (int): Length of the rectangle.
        width (int): Width of the rectangle.
        color (str): Fill color of the rectangle.
    """
    turtle.fillcolor(color)
    turtle.begin_fill()
    
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)

    turtle.end_fill()

# Function to draw a table
def draw_table(length, width, color):
    """
    Draws a table with specified length, width, and color, and draws four legs.
    
    Parameters:
        length (int): Length of the table.
        width (int): Width of the table.
        color (str): Color of the table.
    """
    # Move turtle to position for drawing table
    turtle.penup()
    turtle.goto(-length/2, -width)  # Move to bottom center of table
    turtle.pendown()
    
    # Draw table top
    draw_rectangle(length, width, color)
    
    # Draw legs manually, positioning turtle accordingly
    leg_height = 50  # Leg height is fixed
    leg_width = 10   # Leg width is fixed
    
    # Leg 1 (Bottom left)
    turtle.penup()
    turtle.goto(-length/2+10, -width)  # First leg position
    turtle.right(90)
    turtle.pendown()
    draw_leg(leg_width, leg_height)

    # Leg 2 (Bottom right)
    turtle.penup()
    turtle.goto(-10, -width) # Second leg position
    turtle.pendown()
    draw_leg(leg_width, leg_height)

    # Leg 3 (Top left)
    turtle.penup()
    turtle.goto(20,-width)  # Third leg position
    turtle.pendown()
    draw_leg(leg_width, leg_height)

    # Leg 4 (Top right)
    turtle.penup()
    turtle.goto(length/2 ,-width)  # Fourth leg position
    turtle.pendown()
    draw_leg(leg_width, leg_height)

# Function to draw a table leg (reusable for all legs)
def draw_leg(width, height):
    """
    Draws a single table leg with specified width and height.
    """
    turtle.right(90)  # Turn downward to draw leg
    draw_rectangle(width, height, "brown")  # Leg size fixed
    turtle.left(90)

# Function to draw the cake layers
def draw_cake():
    turtle.speed(3)

    # Bottom layer (largest)
    lay1_h = int(input("Enter width of first layer: ")) #width of layer
    lay1_col = input("Enter colour of first layer: ") #colour of layer
    turtle.penup()
    turtle.goto(-(lay1_h/2),0)  # Start position for the bottom layer
    turtle.left(90)
    turtle.pendown()
    draw_rectangle(lay1_h, 10, lay1_col)  # Width: 200, Height: 50

    # Middle layer
    lay2_h = int(input("Enter width of second layer: ")) #width of layer
    lay2_col = input("Enter colour of second layer: ") #colour of layer
    turtle.penup()
    turtle.goto(-(lay2_h/2),10 )  # Start position for the middle layer
    turtle.pendown()
    draw_rectangle(lay2_h, 10, lay2_col)  # Width: 160, Height: 50

    # Top layer (smallest)
    lay3_h = int(input("Enter width of third layer: ")) #width of layer
    lay3_col = input("Enter colour of third layer: ") #colour of layer
    turtle.penup()
    turtle.goto(-(lay3_h/2), 20)  # Start position for the top layer
    turtle.pendown()
    draw_rectangle(lay3_h, 10, lay3_col)  # Width: 120, Height: 50
    
    
# Setup the turtle
turtle.setup(500, 500)
turtle.bgcolor("white")


# Function to draw a candle on top of the cake
def candle():
    
    turtle.penup()
    turtle.goto(-1,30)
    turtle.pendown()
    draw_rectangle(2,5, 'orange')
    
    
# Function to set the background color
def set_background_color(color):
    """
    Sets the background color of the turtle window.
    
    Parameters:
        color (str): The background color.
    """
    turtle.bgcolor(color)


#  Function to adjust the canvas size and coordinate system
def setup_canvas(table_length, table_width):
    """
    Sets up the canvas size and coordinates to fit the table and cake.
    
    Parameters:
        table_length (int): Length of the table.
        table_width (int): Width of the table.
    """
    # Adjust the canvas size to ensure all elements fit
    turtle.screensize(canvwidth=table_length + 200, canvheight=table_width + 200)
    
    # Adjust the world coordinates so that the origin is at the center
    turtle.setworldcoordinates(-table_length // 2 - 50, -table_width // 2 - 50, 
                               table_length // 2 + 50, table_width // 2 + 50)


# Function to draw decorations (balloons)
def draw_decorations():
    turtle.speed(1)

    # Drawing a balloon
    def draw_balloon(x, y, color):
        turtle.penup()
        turtle.goto(x, y)
        turtle.pendown()
        turtle.fillcolor(color)
        turtle.begin_fill()
        turtle.circle(15)  # Balloon size
        turtle.end_fill()

        # Drawing the string of the balloon
        turtle.penup()
        turtle.goto(x, y )
        turtle.pendown()
        turtle.goto(x, y -30)

    # Drawing multiple balloons 
    draw_balloon(-50, 25, 'red')   # Balloon 1
    draw_balloon(50, 25, 'blue')   # Balloon 2
    
    
# Writing "Happy Birthday" text between the balloons
def happybirthdaytext():
    turtle.penup()
    turtle.goto(0, 40)  # Position the text above the cake and between the balloons
    turtle.pendown()
    turtle.write("Happy Birthday!", align="center", font=("Arial", 16, "bold"))


#function to ask the user to enter any key to close the drawing
def close():
        print("Press any key to exit. ")
        turtle.bye()
        
        
# Main function to draw the scene
def main():
    
    # Function for the turtle to detect users keyboard input
    turtle.listen()

    print("Your cake is loading! Happy Birthday!")
    
    # Ask user for inputs
    table_length = int(input("Enter table length (10-100): "))
    table_width = int(input("Enter table width (10-100): "))
    table_color = input("Enter table color: ")
    
    background_color = input("Enter background color: ")

    # Set up the canvas based on table size
    setup_canvas(table_length, table_width)
    
    # Set background color
    set_background_color(background_color)
    
    # calling the functions: table, cake, and candles, decoration, and birthday text
    draw_table(table_length, table_width, table_color)
    draw_cake()
    candle()
    draw_decorations()
    happybirthdaytext()
    turtle.onkeypress(close)
    turtle.done()
    

main()