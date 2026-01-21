import time
import random
# 1. Think of a riddle
# 2. Using the while loop, ask the user the riddle and
#    check the answer
# 3. While answer is not correct, repeat the question
# Riddle: I have cities, but no houses. I have mountains, but no trees. I have water, but no fish. What am I?
# ans = "Map"
# attempt = 0 
# while True:
#     userans = input("I have cities, but no houses. I have mountains, but no trees. I have water, but no fish. What am I? Please put your answer with the first letter capital.\n")
#     if userans == ans:
#         print("Correct.")
#         break
# print("hi")
# time.sleep(5)
# print("bye")

## Task 1: Study Timer
# **Task: Write a program that acts as a study timer**
# 1. The user must input how many minutes they plan to study
# 2. Use a while loop to count down the minutes
# 3. Display "Good job!" once the timer is up

# Hint: you will need the time.sleep(). However this function
# only takes in seconds.
# You will need to write a conversion algorithm to change
# # minutes to seconds.
# times = int(input("How many minutes do you wish to study for?"))

# while times != 0:
#     print(times)
#     time.sleep(60)
#     times-=1
# print("Ended")
## Task 2: Allowance Savings Tracker
# **Task: Write a program to track how much you save, and
# inform you when your savings is more than $100**
# 1. Create a variable called savings
# 2. Using a while loop, ask how much money you save every
#    day
# 3. While savings is less than 100, you continue to save
# 4. Exit the program when savings is more than 100 and
#    congratulate the user.
# savings = " "
# total = 0
# while True:
#     savings = input("How much money did you save in numerals?")
#     total += int(savings)
#     print("You have saved " + str(total) + " so far.")
#     if total >= 100:
#         print("You have reached your goal!")
#         break
## Task 3: Multiplication Quiz
# **Task: Ms Tan, your math teacher knows that you are a
# programming whiz,
# she has asked you to help code a multiplication quiz for
# the class to practice.**

# Here are her requirements:
# 1. Students have to answer 15 questions in total
# 2. Students have 3 lives (chances). i.e. they can get the
#    question wrong 3 times.
# 3. The questions will be in this format: "What is 3 x 19? ". 
# 4. The numbers for each question will be randomly generated
#    and between the range of 2 to 20.
# 5. If the student answers correctly, move on to the next
#    question
# 6. If the student answers wrongly, minus 1 life, and ask
#     the question again.
# 7. If the student has no more lives, exit and print
#     "GO AND SEE MS TAN FOR REMEDIAL"
lives = 3
for i in range(1,15):
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    ans = a * b
    user = input(str(a) + "x" str(b) + "?")
