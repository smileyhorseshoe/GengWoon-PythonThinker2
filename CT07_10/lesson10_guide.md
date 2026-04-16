# Lesson 10 - Bouncing Ball

## Task 1: Even or Odd
Create a function that takes in a number and returns whether it is even.

1. Create a function named ‘is_even()’
2. If the number is even, the function should return ‘True’
3. If the number is odd, the function should return ‘False’
4. Using the ‘is_even()’ function, loop through a list of numbers and print them out in this format:“3 is an odd number”“9 is an odd number”“2 is an even number”

## Task 2: Age Group
Create a function that will take in someone’s age and return either of the following based on the age provided:
- ‘Child’ (Below 13)
- ‘Teen’ (14-20)
- ‘Adult’ (21-64), or
- ‘Senior’ (65 and above)

Define the function ‘age_group()’ with one parameter: ‘age’.
Use ‘if-elif-else’ statements to return the appropriate age group based on the ‘age’ parameter.

## Task 3: Quadruple the Number 
Create a function that takes in a number and quadruples it.

Create a function named quadruple_number() that takes in 1 parameter
The function should take in a number, and return the quadrupled value of the number
Using the quadruple_number() function, print the quadruples of the following numbers:
- 105 (ans: 420)
- 24 (ans: 96)
- 402 (ans: 1608)
- 594 (ans: 2376)

## Task 4: Sum of squares - Function within a function

### Task 4a
Create a function ‘square()’ that will take in a number and return the squared value of the number. Squared is when the number is multiplied by itself.

For example, “5 squared” or 5² = 5x5 = 25

Example:
square(5) >>> 25
Square(7) >>> 49
square(3) >>> 9

### Task 4b
Create a function ‘sum_of_squares()’ that will take in 2 numbers and return the sum of each of the number squared.

You must use the  ‘square()’ function within the ‘sum_of_squares()’ function.

Example:
sum_of_squares(3, 4) >>> 25
sum_of_squares(2, 7) >>> 53
sum_of_squares(9, 5) >>> 106

## Task 5: Creating a turtle window
By creating and using the following function, create a turtle window that is 300(w) x 500(h):
- setup_screen(screenWidth, screenHeight)

You will require the following:
1. import turtle
2. turtle.Screen()
3. .setup(width=???, height=???)
4. return
5. ‘screenWidth’ variable
6. ‘screenHeight’ variable

## Task 6: Creating a turtle object
By creating and using the following function, create a blue circular turtle object with its pen lifted: 
- create_blue_ball()

You will require the following:
1. turtle.Turtle()
2. .shape()
3. .color()
4. .penup()
5. return

## Task 7: Moving turtle object
By creating and using the following function, move the turtle object by ‘dx’ and ‘dy’ in a forever loop: 
- move_ball(ball, dx, dy)

You will require the following:
1. .setx()
2. .xcor()
3. .sety()
4. .ycor()
5. ‘dx’ variable
6. ‘dy’ variable

## Task 8a: Detecting edge (x-axis)
By creating and using the following function, reverse the x-direction that the turtle object is moving when it touches the left/right side of the window: 
- check_x(ball, screenWidth)
- Returns ‘True’ if ball is beyond window in the x-axis

You will require the following:
1. .xcor()
2. screenWidth/2
3. or
4. -screenWidth/2
5. *= -1

## Task 8b: Detecting edge (y-axis)
By creating and using the following function, reverse the y-direction that the turtle object is moving when it touches the top/bottom side of the window: 
- check_y(ball, screenHeight)
- Returns ‘True’ if ball is beyond window in the y-axis

You will require the following:
1. .ycor()
2. screenHeight/2
3. or
4. -screenHeight/2
5. *= -1

## Challenge: Features to implement
1. Have a line trail that the turtle object leave behind as it bounces around
2. Change the following each time the turtle object bounces:
- Colour of the turtle object
- Speed of the turtle object (faster/slower)
- Shape of the turtle object
3. Use a variable to count the number of times the ball has bounced
4. Exit the loop when the ball bounces 50 times.
5. Use the time library to keep the program running for ‘x’ seconds determined by the user