"""
============================================================
Q2. Odd or Even Checker
============================================================
You are given a list of numbers.
The program must check whether each number is odd or even.

num_list = [2944, -5490, 2357, -2619, 1177, 451, -8299, 2533, 4682, -6040, 0]

Program Requirements:
- Write a function is_even(num)
- If the number is even, return True
- If the number is odd, return False
- Use a for loop to go through the list
- Call the function for each number

Print the result exactly in this format:
    2944 is even.
    -2619 is odd.
    ...

============================================================
"""

# ============================================================
# Step 1: Create the function
# ============================================================
def is_even(num):
    if num%2 == 0:
        return True
    if num%2 ==1:
        return False

# ============================================================
# Step 2: Create the list
# ============================================================

num_list = [2944, -5490, 2357, -2619, 1177, 451, -8299, 2533, 4682, -6040, 0]


# ============================================================
# Step 3: Loop through the list and use the function
# ============================================================
for i in num_list:
    if is_even(i) == True:
        print(f"{i} is even.")
    else:
        print(f"{i} is odd.")
    