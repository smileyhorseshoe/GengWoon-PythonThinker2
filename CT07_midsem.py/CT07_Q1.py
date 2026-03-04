# ============================================================
# Q1. Hero Quest
# ============================================================
# A hero goes on an adventure, starting at Full Health.
# He fights monsters and loses health randomly each round.

# Requirements:
# - Start with 100 health
# - Print starting message
# - Lose between 1 to 15 health each round (random)
# - Use a while-loop
# - Continue until health <= 0
# - Print total number of battles fought

# ============================================================
# """

# # ============================================================
# # Step 1: Import required module
# # ============================================================

import random

# # ============================================================
# # Step 2: Initialize variables
# # ============================================================
health = 100
battles = 0
deduct = 0

# # ============================================================
# # Step 3: Print starting message
# # ============================================================
print(f"The hero is going on another adventure.")


# ============================================================
# Step 4: Create while-loop for battles
# ============================================================
# - Randomly reduce health between 1 and 15
# - Increase battle counter
# - Print updated health
# ============================================================
while True:
    print("On his way, he finds many monsters. He begins to fight them in a battle.")
    deduct = random.randint(1,15)
    health = health - deduct
    print(f"The hero has lost {deduct} health! He has {health} health remaining.")
    if health <= 0:
        break
    battles +=1
    print("The hero has won the battle and is going on with his journey...")

# ============================================================
# Step 5: Print final result
# ============================================================
# Print in this format:
# He fought xxx battles, and died
# ============================================================
print(f"The hero fought {battles} battles and died.")