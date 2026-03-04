# ============================================================
# Q2. Food Order System
# ============================================================
# Write a PYTHON program that simulates a restaurant order
# system using list and while loop.

# Requirements:
# - Use a while loop
# - Ask: "What would you like to order?"
# - Store each order into a list
# - Stop when user enters "end"
# - After ending, print all orders in numbered format

# ============================================================
# """

# # ============================================================
# # Step 1: Initialize variables
# # ============================================================
order = []
item = " "
index = 0
# # ============================================================
# # Step 2: Create a loop
# # ============================================================
while True:
    item = input("What would you like to order?")
    if item == "end":
        break
    order.append(item)


# # ============================================================
# # Step 3: Print the final order summary
# # ============================================================
# # Print the final order in this format:
# # You have ordered the following:
# # 1. Item1
# # 2. Item2
# # 3. Item3
# # ============================================================
print("You have ordered the following:")
for item in order:
    index +=1
    print(f"{index}. {item}") 
