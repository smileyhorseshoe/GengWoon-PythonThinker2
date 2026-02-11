# print("Hello from lesson 6")
import random
# You are preparing for an upcoming lucky draw session at your
# school. However, there must be no repeating winning numbers.

# Task: Create a program to create 100 random unique numbers in
# a list
# 1. Use a loop to add 100 random numbers into your list.
# 2. Each number added range between 1 to 1000
# 3. Ensure that all the numbers are unique

# **Recap 1b**:
# You have been asked to provide some statistics based on the
# list of numbers generated.

# 1. Using max(), find the highest number from the list
# 2. Using min(), find the lowest number from the list
# 3. Using sum() and len(), find the average from the list
# 4. By importing the 'random' library and using random.choice(),
#    print out a random number from the list.
# 5. Using index(), print out the index of the printed random
#    number.
# winners = [ ]
# for count in range(100):
#     randnum = random.randint(1,1000)
#     if randnum in winners:
#         randnum = random.randint(1,1000)
#     winners.append(randnum)
# print(winners)
# print(f"Max number is {max(winners)}.")
# print(f"Minimum number is {min(winners)}.")
# avg = sum(winners) / len(winners)
# print(f"Average is {round(avg)}.")
## Task 1: A list within a list 

# You are about to graduate and would like to create a database
# to keep all your friend's contact details using a 2d list.

# Sample Code (Copy + Paste the below code):
# contacts = []
# contact1 = ["John", 98453126, "john@gmail.com"]
# contact2 = ["Adam", 93029102, "adam@gmail.com"]
# contact3 = ["Sylvia", 87894032, "sylvia@gmail.com"]
# contacts.append(contact1)
# contacts.append(contact2) 
# contacts.append(contact3)
# print(contacts)
# # for details in contact1:
# #     print(details)
# for contact in contacts:
#     name, phone_number, email = contact
#     print(f"{name}'s email address is: {email} and their phone number is {phone_number}")
# 1. append contact1, contact2, and contact3 into contacts
# 2. Write a nested loop to loop through each contact and print
#    the details for each contact
## Task 2: Student List
# You have been given a 2d list of students from a class
# consisting each student's name and their gender:

# Sample Code (Copy + Paste the below code):
students = [
    ["Olivia", "F"], 
    ["Noah", "M"], 
    ["Emma", "F"],
    ["Liam", "M"], 
    ["Ava", "F"], 
    ["Ethan", "M"],
    ["Sophia", "F"], 
    ["Lucas", "M"], 
    ["Mia", "F"],
    ["Aiden", "M"], 
    ["Isabella", "F"], 
    ["Jackson", "M"],
    ["Amelia", "F"], 
    ["Logan", "M"], 
    ["Lily", "F"]

    
]
boys = [ ]
girls = [ ]
for student in students:
    name, gender = student
    # print(f"Gender of {name}: {gender}.")
    if gender == "F":
        girls.append(name)
    elif gender == "M":
        boys.append(name)
# ### the above is a nested list. Study and discuss it before we
# ### move on.

# 1. Write a for loop to print out the names of each student and
#    the gender beside.
   
#    e.g. Olivia F
        # Noah M
## Task 3: Boys and Girls

# Based on the class list given in the previous task, separate
# the class into 2 lists of boys and girls.

# 1. Create 2 more lists called boys and girls.
# 2. Loop through the 'students' list from the previous task
#    a. if the gender is a boy, add the name into the boys list
#    b. if the gender is a girl, add the name into the girls list
# 3. Write a for loop and name all the boys
# 4. Write a for loop and name all the girls
# 5. Print out how many boys and girls there are
print("The boys are:")
for name in boys:
    print(name)
print("The girls are:")
for name in girls:
    print(name)
print(f"There are: {len(boys)} boys and {len(girls)} girls in this class.")
