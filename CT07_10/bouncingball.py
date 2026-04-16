import turtle
import random

# get ready the window
def setup_screen(screenWidth, screenHeight):
    window = turtle.Screen()
    window.setup(width=screenWidth, height=screenHeight)
    return window

# call 1st function
myscreen = setup_screen(300, 500)

# get ready a ball
def create_blue_ball():
    t = turtle.Turtle()
    t.shape("circle")
    t.color("blue")
    t.penup()
    return t

# call 2nd function
mypet = create_blue_ball()
mypet.forward(80)

# call 3rd function
# today continue from here
# Task 7/8 **
# ## Task 8a: Detecting edge (x-axis)
# By creating and using the following function, reverse the x-direction that the turtle object is moving when it touches the left/right side of the window: 
# - check_x(ball, screenWidth)
# - Returns ‘True’ if ball is beyond window in the x-axis

# You will require the following:
# 1. .xcor()
# 2. screenWidth/2
# 3. or
# 4. -screenWidth/2
# 5. *= -1
def check_x(ball,screenWidth):
    if ball.xcor() > (screenWidth/2-15) or ball.xcor() < (-screenWidth/2+15):
        return True
    return False
# By creating and using the following function, reverse the y-direction that the turtle object is moving when it touches the top/bottom side of the window: 
# - check_y(ball, screenHeight)
# - Returns ‘True’ if ball is beyond window in the y-axis

# You will require the following:
# 1. .ycor()
# 2. screenHeight/2
# 3. or
# 4. -screenHeight/2
# 5. *= -1
def check_y(ball,screenHeight):
    if ball.ycor() > (screenHeight/2-15) or ball.ycor() < (-screenHeight/2+15):
        return True
    return False

def move_ball(ball,vx,vy):
    ball.setx(ball.xcor()+vx)
    ball.sety(ball.ycor()+vy)

colours = ["red","orange","pink","purple","indigo","cyan"]
randcolor = random.randint(0,5)
mypet.color(colours[randcolor])
vx = random.randint(2,6)
vy = random.randint(2,6)
mypet.pd()
while True:
    move_ball(mypet,vx,vy)
    if check_x(mypet,300):
        vx*= -1
    if check_y(mypet,500):
        vy*=-1

myscreen.mainloop() # this is always the last line