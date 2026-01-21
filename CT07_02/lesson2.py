import time
# print("Hello from lesson 2")
# Print numbers till 13, odd numbers only
# for i in range(1,14,2):
#     print(i)
#-----------------------------
# Recap
# print("Loop One")
# for i in range(0,21):
#     print(i)
# print("Loop Two")
# for i in range(1,31):
#     print(i)
# print("Loop Three")
# for i in range(2,25,2):
#     print(i)
# -----------------------------
counter = 0
# while counter < 6:
#     print(counter)
#     counter+=1

# while counter < 21:
#     print(counter)
#     counter +=1
# while counter < 31:
#     print(counter)
#     counter +=1
# counter = 2
# while counter < 25:
#     print(counter)
#     counter +=1
# while counter < 11:
#     print(counter)
#     counter +=1
#     if counter ==6:
#         break
# num = 10
# while num != 0:
#     print(num)
#     num-=1
#     time.sleep(1)
#     if num == 4:
#         break
# else:
#     print("Happy New Year!")
# print("no.")
# number = 0
# while number != 10:
#     print(number)
#     number+=1
#     time.sleep(1)
#     if number == 6:
#         break
# else:
#     print("Count has reached 10. Goodbye.")
# print("no.")
# pth = ""
# topping = ""
# while True:
#     topping = input("Please enter your desired toppings.")
#     if topping == "end":
#         break
#     pth = pth + " " + topping

# print(pth)
# ## Task 5: General Knowledge Quiz
# **Task: Create a program to quiz users on their general
# knowledge**

# Using the while loop, ask 3 general knowledge questions
# 1. Using input ask the question
# 2. While answer is not correct, repeat the question.
# 3. Move on to the next question when the answer is correct

# Bonus:
# 1. Add a score system
# 2. Add an ability for users to skip by saying “skip”
# 3. Disqualify user when they have tried too many times
print("Welcome to the General Knowledge Quiz!")
print("You have five tries per question. If you with to skip, please put 'skip' as your answer.")
try1 =0
try2 =0
try3 =0
ans1 ="2"
ans2 ="Blue Whale"
ans3 ="Kuala Lumpur"
points = 0
while True:
    userans = input("What is 1+1?\n")
    if userans == ans1: 
        points = points + 1
        break
    elif try1 == 5:
        print("You failed.")
        break
    elif userans == "skip":
        print("Skipped.")
        break
    try1 +=1
    print("You have used up " + str(try1) + " out of five tries." )
while True:
    userans1 = input("What is the largest Mammal in the world? Please give your answer with the starting letter of both words capitalized\n")
    if userans1 == ans2:
        points+=1
        break
    elif try2 == 5:
        print("You failed.")
        break
    elif userans1 == "skip":
        print("Skipped.")
        break
    try2+=1
    print("You have used up " + str(try2) + " out of five tries." )
while True:
    userans2 = input("What is the capital of Malaysia?\n")
    if userans2 == ans3:
        points+=1
        break
    elif try3 == 5:
        print("You failed.")
        break
    elif userans2 == "skip":
        print("Skipped.")
        break
    try3 +=1
    print("You have used up " + str(try3) + " out of five tries." )
print("You have reached the end of this quiz.")
time.sleep(1)
print("Your score was:" + str(points))
time.sleep(1)
print("Your answers: " + "Question 1: " + userans + ". Question 2: " + userans1 + ". Question 3: " + userans2)
time.sleep(3)
print("THE ANSWERKEY " + "Question 1: "+ ans1 + " Question 2: " + ans2 + " Question 3: " + ans3)

print("BYE!!")