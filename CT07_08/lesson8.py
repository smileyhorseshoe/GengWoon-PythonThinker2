# Lesson 8 - Input Validation

# # Recap 1: List Manipulation
# You have a list of student index numbers who attended the Math Enrichment class. 
# However, some students’ attendance were recorded more than once due to a human error.
# Your task is to clean the list and produce a list of unique Student Indexes

# Given a list of student index numbers (with duplicates), create a cleaned list where each student appears once.
# Sort the cleaned list in ascending order.
# - Print the final list and also print how many duplicates were removed.
# - Print the count of how many students attended the Math Enrichment Class.
# duplicate_count = 0
# student_indexes = [1042, 1099, 1031, 1120, 1075, 1042, 1108, 1019, 1063, 1099, 1156, 1027, 1084, 1111, 1031, 1143, 1055, 1108, 1070, 1132, 1055, 1168, 1020, 1084, 1175]
# unique_list = []
# for i in student_indexes:
#     if i not in unique_list:
#         unique_list.append(i)
#     else:
#         duplicate_count+=1
# sorted_list = sorted(unique_list)
# print(f"{sorted_list} is the final list, {duplicate_count} were removed, {len(sorted_list)} attended the lesson.")

# group all the student indexes such that it is in ascending order 
# if there is more than once, put them together, for example if there is two 1042, they should be in [1042,1042]
# the final result is a nested list where by those with duplicate are in [1042,1042] manner 
# and those unique would be in [1043] manner and the nested list will be [[1042,1042], [1043], ...]
# for i in student_indexes:
#     if i in unique_list:
#         unique_list.append(i)
# sorted_list = sorted(unique_list)
# print(sorted_list)
# for i in student_indexes:
#     if i not in unique_list:
#         unique_list.append(i)
#     elif i in unique_list
# sorted_list = sorted(unique_list)
# # Task 1: Data Format Check

# ## Task 1a
# Ask the user to input their first name until it is a valid name. 
# A valid name only contains alphabets.
# Keep asking for a name until a valid name is input.
# first_name = ""
# first_name = input("What is your first name?")
# while True:
#     first_name = input("What is your first name?")
#     if first_name.isalpha():
#         break

# print(f"Your first name is {first_name}")
# ## Task 1b
# Ask the user to input their age until it is a valid number. 
# Keep asking for their age until a valid number is input.
# while True:
#     number = input("What is your number?")
#     if number.isdigit():
#         break
#     else:
#         print(f"Please only use numbers.")
# print(f"Your number is {number}")
# ## Task 1c
# Ask the user to input a valid username. A valid username must contain alphabets and numbers, but not contain special characters
# while True:
#     username = input("What is your desired username?")
#     if username.isalnum():
#         break
#     else:
#         print(f"Please only use letters and numbers.")
# print(f"Your username is {username}")
# # Task 2: Length Check (using a while loop)

# ## Task 2a
# Ask the user to input their phone number until it is valid using a while loop.
# Make sure to check if the input is the correct data type as well!
# while True:
#     phone_num = input("What is your phone number?")
#     if len(phone_num) ==8 and phone_num.isdigit:
#         break
#     else:
#         print("Please enter a valid phone number.")
# print(f"Your phone number is: {phone_num}")
# ## Task 2b
# Ask the user to a username and check if it is between 5 to 18 characters long.
# while True:
#     username = input("Please enter a username.")
#     if len(username) <=18 and len(username) >= 5 and username.isalnum():
#         break
#     else:
#         print("Please enter a valid username.")
# print(f"Your username is {username}")
# # Task 3: Range Check (using a while loop)

# ## Task 3a
# Ask the user to input their birth year and check if it is between 1900 and the current year. Keep asking until a correct value is given.
# while True:
#     by = input("What is your birth year?")
#     if by.isdigit() and int(by) >=1900 and int(by) <= 2027 :
#         break
#     else:
#         print("Please enter a valid birth year.")
# print(f"Your birth year is {by}")
# ## Task 3b
# Ask the user to input their volume setting and check if it is between 0 and 100.
# while True:
#     volume = input("What is your volume?")
#     if volume.isdigit() and int(volume) >= 0 and int(volume) <= 100:
#         break
#     else:
#         print("Please input a valid number from 0 to 100.")
# print(f"Your volume is {volume}")
# # Task 4: Mocking Text Generator
# Create a program that will turn regular sentences into a “SpongeBob Mocking” meme.
# For example, the program will turn “Hello my name is James” into “HeLlO mY nAmE iS jAmEs”

# 1. Using input(), ask the user for a sentence
# 2. Use loops to iterate through each letter in the sentence
# 3. Alternate between .upper() and .lower() for each letter
# 4. Print the result.
# sentence = input("Please enter a sentence.")
# mocking_sentence = ""
# alternate = True
# for char in sentence:
#     if char.isalpha():
#         if alternate:
#             mocking_sentence = mocking_sentence + char.upper()
#             alternate = False
#         else:
#             mocking_sentence = mocking_sentence + char.lower()
#             alternate = True
#     else:
#         mocking_sentence = mocking_sentence + char
# print(mocking_sentence)
# # Task 5: Slice String


# Slice the string and print these words:
# a. SING
# b. GAP
# c. PORE
# d. SNAOE
# sentence = "SINGAPORE"
# a = sentence[0:4]
# print(a)
# b = sentence[3:6]
# print(b)
# c = sentence[6:]
# print(c)
# d = sentence[0::2]
# print(d)
# # Task 6: Palindrome
# Ask the user for an input and check if it is a palindrome, until the input is ‘end’.
# while True:
#     word = input("Enter a word.")
#     if word == "end":
#         break
#     if word == word[::-1]:
#         print(f"'{word}' is a palindrome!")
#     else:
#         print(f"'{word}' is not a palindrome!")
#     print(word[::-1])
# You can try this list of words:
# - civic, kayak, level, madam, radar, refer, rotator, tenet, racecar, deified, stats, wow

# # Task 7: Presence and Existence Checks
# You are hosting a Birthday Party and have invited your friends.

# Create a list with your friends’ names
# lof = ["Alice", "Bob", "Carl", "Dylan"]
# while True:
#     name = input("What is your name?")
#     if name == "":
#         print("Please input a name.")
#     elif name not in lof:
#         print("You are not invited. GET OUT!")
#     elif name in lof:
#         print("Welcome! Please enter.")
#         break
# - Name is entered (presence check)
# - Name is in your friend list (existence check)

# Ask for an input again if a name was not entered.
# Accept the visitor if they are in the list, else deny their entry.

# # Task 8: Format Check
# Ask the user to input their NRIC you need to check:
# 1. First and last character are alphabets in upper case
# 2. First letter must be S, T, F, G, or M.
# 3. Have 7 digits between the alphabets
# 4. Be 9 characters long
# FLA = False ## First and Last Variable
# SL = False ## Starting letter
# D  = False ## 7 Digits
# L = False ## Length
# NE = False ## Not Empty
# NRIC = input("What is your NRIC?")
# if len(NRIC) == 9:
#     L = True
#     if NRIC[0].isalpha() and NRIC[0].isupper() and NRIC[8].isalpha() and NRIC[8].isupper():
#         FLA = True
#     if NRIC[0] == "S" or NRIC[0] == "T" or NRIC[0] == "F" or NRIC[0] == "G" or NRIC[0] == "M":
#         SL = True
#     if NRIC[1:8].isdigit():
#         D = True
#     if NRIC != "":
#         NE == True
        
# # -------
# if FLA == False:
#     print("Please make sure the starting and ending alphabet is uppercase.")
# if SL == False:
#     print("Please make sure starting letter is correct.")
# if D == False:
#     print("Please ensure that your NRIC has 7 digits.")
# if L == False:
#     print("Please ensure that the length of your NRIC is correct")
# if NE == False:
#     print("NRIC cannot be left blank.")
# if FLA == True and SL == True and D == True and L == True and NE == True:
#     print("You pass.")

# # Task 9: Password Validation
# A website requires all passwords to
# 1. Be at least 8 characters long
# 2. Contain an upper and lower case
# 3. Contain a number
# 4. No other characters except alphabets or numbers.

# Write a program that will ask the user for a password, and check if the password fits all criteria

# You may use some of the following passwords to test your program:
# - PassW0rd
# - H3ll0W0r1d
# - BestF00d
# - pa55Me