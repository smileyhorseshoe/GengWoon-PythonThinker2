print("Hello from lesson 1")

# Recap One:
# Make a Variable for: GLass, Plastic and Paper respectively.
# Ask the user what the material is and check against the list of variable
# Sort it into the bin with the corresponding material
# example:
# Input: Glass
# Bin: Glass
# Print: Done
# If no valid input/material was detected(else): print Your Material is not recyclable!
# Repeat till all are sorted
#  ----------------------
## Recap 2: Variables & Mind map
# Use mindmap to think about the number of variables you need for
# the following. Then, create a program that does the following:

# You just had lunch at a sushi restaurant and have to calculate
# the total amount you have spent. Different coloured plates
# costs different as shown below:

# Red = $1
# Blue = $2
# Green = $3

# You have ordered a total of 3 red plates, 5 blue plates,
# and 4 green plates. Calculate and print the total amount you
# have spent:
# ----------------------------------------
# Red = 1
# Blue = 2
# Green = 3
# Total = (Red*3) + (Blue*5) + (Green*4)
# print("You spent $" + str(Total) + " on lunch today!")
# ----------------------------------------
# ## Recap 3: Debugging Average Score Program
# There is a total of 3 bugs in the following program.
# Identify and fix the bugs:
# ----------------------------------------
# score_one = 80
# score_two = 90
# score_three = 75

# total = score_one + score_two + score_three

# average_score = total / 3

# student_name = "Alex"

# print("Average score for " + student_name + " is: " + str(average_score))
# ------------------------------------------
## Recap 4: If..elif..else & Flowchart
# Write a program that asks the user to input a score
# (as an integer) and then assigns a grade based on that score.
# Use the following grading scheme:

# If the score is 75 or higher, the grade is 'A'.
# If the score is between 60 and 74 (inclusive), the grade is 'B'.
# If the score is between 50 and 59 (inclusive), the grade is 'C'.
# Any score below 50 will be graded as 'Fail'.

# Use flowchart to draw out all decisions that are to be made
# before starting on your code.
# -------------------------------------------------
score = int(input("Please input your score."))
if score >= 75:
    print("Your Score is an A.")
elif score >=60 and score <=74:
    print("Your score is a B.")
elif score >=50 and score <=59:
    print("Your score is a C.")
else:
    print("You failed.")