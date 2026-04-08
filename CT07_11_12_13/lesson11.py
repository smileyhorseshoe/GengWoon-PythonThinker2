# print("Hello from lesson 11_12_13")

# Lesson 11 - Turtle Race

## Task 1: Turtle Race
# We are creating a turtle racing program. In this program, there
# will be 3 turtles at the starting line. The user will be given
# a choice on which one will win.

# Once the user has made their choice, the turtles will move in
# random distances and directions toward the finishing line until
# one of them crosses it.

# We will work on each section of the program one at a time until
# we have a complete program.
# **Task 1a**: Setting Up the Screen
# Lets start by creating a window that is "forestgreen" in colour,
# and 600 in width and height

# 1. Import the 'turtle' module
# 2. Assign 'turtle.Screen()' to a variable 'window' to create a
#    window for your turtle graphics.
# 3. Use '.setup(width=???, height=???)' on 'window' where '???'
#    is the desired width and height of the window
# 4. Set the background colour of the window to "forestgreen"
#    using '.bgcolor()'
# Tip: Use '.mainloop()' at the end of your program to keep the
# window open
# You should see this when you run the program! (Refer to slides)
# **Task 1b**: Drawing the finish line
# Adding on to your previous answer, create a line of black
# squares at y = 250 by creating a black square turtle object
# and stamping it from x = -300 to x = 300 at 25 pixel-
# intervals

# 1. Create a turtle object named 'pen'
# 2. Lift the pen up
# 3. Using '.shape()', set the turtle object's shape to "square"
# 4. Using '.sety()', set turtle object's y position to 250
# 5. Using a 'for i in range()' loop, use the 'i' variable to
#    create a stamp of 'pen' turtle object from x = -300 to
#    x = 300 at 25-pixel intervals:
#         a. Set 'pen' turtle's x coordinate using '.setx()'
#         b. Stamp a copy of 'pen' turtle at its current
#            position using '.stamp()'

# Tip: Use '.mainloop()' at the end of your program to keep the
# window open

# You should see this when you run the program! (Refer to slides)

# **Task 1c**: Drawing the start line
# Adding on to your previous answer, use the 'pen' turtle object
# you have created earlier to draw a horizontal yellow start
# line at y = -250.

# 1. Using '.goto()', set 'pen' turtle's coordinates to
#    (-300, -250)
# 2. Using the following commands, set the colour of 'pen' to
#    "yellow", set heading to 0 and move forward by 600
#    before hiding the turtle:
#         a. '.pencolor()'
#         b. '.pendown()'
#         c. '.seth()'
#         d. '.forward()'
#         e. '.hideturtle()'

# Tip: Use '.mainloop()' at the end of your program to keep the
# window open

# You should see this when you run the program! (Refer to slides)

# **Task 1d**: Create Sally the turtle
# Adding on to your previous answer, create a red, turtle-shaped
# turtle object 'Sally' will be one of the turtle racers.
# Position Sally at the starting position of (0, -250) and put
# "Sally" above the 'Sally' turtle object.

# 1. Using 'turtle.Turtle()', create a 'Sally' turtle object
# 2. Lift the pen using '.penup()'
# 3. Using '.seth()', set 'Sally' turtle's heading to 90
# 4. Using '.shape()', set 'Sally' turtle's shape to "turtle"
# 5. Using '.color()', set 'Sally' turtle to "red"
# 6. Using '.goto()', move 'Sally' turtle to (0, -250)
# 7. Using '.write("Sally", align="center", font=('Arial', 20))',
#    put "Sally" above Sally the turtle

# Tip: Use '.mainloop()' at the end of your program to keep the
# window open

# You should see this when you run the program! (Refer to slides)

# **Task 1e**: Configure Bob and Keith turtles
# Adding on to your previous answer, repeat what you have done
# to set up Sally the turtle to also create the following
# turtles and position them at the specified coordinates:
# 1. Bob:
#     Colour: "blue"
#     Starting position: (-200, -250)
# 2. Keith:
#     Colour: "white"
#     Starting position: (200, -250)

# Tip: Use '.mainloop()' at the end of your program to keep the
# window open

# You should see this when you run the program! (Refer to slides)

# **Task 1f**: Input to guess the race winner
# Adding on to your previous answer, ask the user to guess the
# winner and store the user's response in the 'guess' variable

# 1. Using 'input()', ask the user to "Guess the winner! " in
#    the console.
# 2. Store the user's response in the variable 'guess'

# Tip: Use '.mainloop()' at the end of your program to keep the
# window open

# You should see this when you run the program! (Refer to slides)

# **Task 1g**: Racing loop
# Adding on to your previous answer, import the 'random' library
# and create a forever loop that will set each racing turtle's
# heading and number of steps forward randomly until one of them
# crosses y=250 where the finish line is.

# 1. Initiate a variable 'winner' and assign it an empty string
# 2. Set Bob, Sally, and Keith's pen down.
# 3. In a forever loop:
#     a. Use '.seth()' and '.randint()' to set each racing
#        turtle's heading to between 75 and 115 randomly
#     b. Use '.forward()' and 'randint()' to move each racing
#        turtle forward by between 1 and 20 randomly
#     c. Using '.ycor()', create an 'if..elif..elif' statement
#        that checks if any of the racing turtle's y coordinate
#        is higher than y = 250.
#             i. If true, set the 'winner' variable to the
#                winning turtle's name and 'break' out of the
#                forever loop.

# Tip: Use '.mainloop()' at the end of your program to keep the
# window open

# You should see this when you run the program! (Refer to slides)

# **Task 1h**: Check if user's guess is correct
# Adding on to your previous answer, check if the user's guess is
# correct by comparing the 'winner' variable to 'guess'. Announce
# if the user got the right answer in the console.

# 1. Using an 'if..else' statement, check if the user's guess is
#    the winner.
#     If the user was right,
#         print "Your guess was correct!"
#     Else,
#         print "The winner was " and "Better luck next
#         time!"

# Tip: Use '.mainloop()' at the end of your program to keep the
# window open

# Your turtle racing program is now complete!
#  Import Libary
import turtle 
import random
# Global Var
screen = turtle.Screen() 
t = turtle.Turtle() 
# Setup
# screen.setup(width=800,height=800)
screen.bgcolor((1,1,0))
# FUNCTIONS
def draw_square():
    # The code below is used to make a, one and only, ONLY A SINGULAR SQUARE
    t.seth(0) ## Set Init. Direction
    t.pendown() 
    for i in range(4):  ## Draw a square(square has 4 sides)
        t.forward(50) ## NOTE IT IS IN PIXELS
        t.right(90) ## Turns right(90 degrees)

t.hideturtle()
# How-to check width and height
width = screen.window_width()
height = screen.window_height()
print(width, height)



# Main Code
t.penup() ## Puts pen up
t.goto(-width/2+10,height/2 - 100)
t.speed(0) ## Sets drawing speed
t.seth(0) ## Set Init. Direction 
t.shape("square")
for i in range(int(-width/2+10),int(width/2),30):
    t.setx(i)
    t.stamp()
t.goto(-width/2, -height /2+100)
t.pencolor("green")
t.pendown()
t.goto(width/2,-height/2+100)


# Make new turtle racer :D
Sally = turtle.Turtle()
Sally.hideturtle()
Sally.shape("turtle")
Sally.seth(90)
Sally.pu()
Sally.color("blue")
Sally.goto(0,-height /2+85)
Sally.write("Sally",align="center",font=("Arial",20))
Sally.showturtle()
Sally.pd()
# Make new turtle racer :D
Bob = turtle.Turtle()
Bob.shape("classic")
Bob.hideturtle()
Bob.seth(90)
Bob.pu()
Bob.color("Red")
Bob.goto(-width/4,-height/2+100)
Bob.write("Bob",align="center",font=("Arial",20))
Bob.showturtle()
Bob.pd()
# Make new turtle racer :D
Keith = turtle.Turtle()
Keith.shape("arrow")
Keith.hideturtle()
Keith.seth(90)
Keith.pu()
Keith.color("Green")
Keith.goto(width/4,-height/2+90)
Keith.write("Keith",align="center",font=("Arial",20))
Keith.showturtle()
Keith.pd()
# GROUP TURTLES IN A LIST
turtles = [Sally,Bob,Keith]
end = False
# da racing loop :D
while True:
    for i in turtles:
        i.seth(random.randint(75,115))
        i.forward(random.randint(1,20))
    # Check if turtle reach finush line
    if i.ycor() > int(height) /2 -100:
        
        print(f"Winner: {winner}")
        

        end = True
        print("End")
    if end == True:
        break
        

turtle.done() ## keeps the window open, you can also do turtle.mainLoop() also known as its DONE
