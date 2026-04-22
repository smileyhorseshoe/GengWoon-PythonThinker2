# # Lesson 12 - Function Practice
import random
# ## Task 1: Build a Game Menu Screen - Functions()
# You will create a “first screen” that prints a title banner, welcome message, rules, and a menu.

# The program must be organised into separate functions

# Each function has one job (title, separator, rules, menu).


# A final function game_intro() will call the functions in order to produce the full page.

# When you run the program, you should see a clean, formatted welcome screen ready for user input later.

# ### Function 1: print_title()
# Function: print_title() — Title Banner + Welcome Text

# This function prints the ASCII art title (students can copy/paste it).
# - After the banner, it prints two welcome lines to set the game story context. (You may change this)
# - It takes no parameters because the title and message are fixed.
# - It has no return value because its job is only to display output.


print("""
     ██████╗  ██████╗  ██████╗███████╗  ██████╗ ██╗   ██╗███████╗███████╗████████╗
    ██╔════╝ ██╔═══██╗██╔══██╗██╔════╝ ██╔═══██╗██║   ██║██╔════╝██╔════╝╚══██╔══╝
    ██║      ██║   ██║██║  ██║█████╗   ██║   ██║██║   ██║█████╗  ███████╗   ██║   
    ██║      ██║   ██║██║  ██║██╔══╝   ██║▄▄ ██║██║   ██║██╔══╝  ╚════██║   ██║   
    ╚██████╗ ╚██████╔╝██████╔╝███████╗ ╚██████╔╝╚██████╔╝███████╗███████║   ██║   
     ╚═════╝  ╚═════╝ ╚═════╝ ╚══════╝  ╚═════╝  ╚═════╝ ╚══════╝╚══════╝   ╚═╝   
""")


# ### Function 2 & 3 : draw_separator() and print_rules()
# 2. draw_separator() — Make the Output Look Neat

# - This function prints "=" * 45 to create a visual divider.

# 3. print_rules() — Show the Rules Clearly

# - This function prints the heading “Rules:” and the 3 rule lines.
# - You can edit the rules anytime without touching the rest of the program.
# - No parameters, no return value — its job is to display fixed text.

# ### Function 4: show_menu()
# show_menu() — Give the Player Choices

# - This function prints the heading “Menu:” and 3 options.
# - Keeping the menu in a function makes it easy to change options later.

# No parameters and no return value — it prints a fixed menu.

# ### Function 5: game_intro()
# game_intro() — Combine Everything in the Right Order

# - This function is your “director” that calls the other functions.
# - It controls the screen layout: 	title → separator → rules → separator → menu → separator.

# If you want to change the order (e.g., menu before rules), you change it here only.

# This is the key idea: small functions + one main function = clean program structure.

# ## Task 2: Build a Quest Board - Functions (params) 
# The program prints a “Quest Board Notice” to the console.
# Each quest looks like a mini poster: header + details + advice.
# Changing the function inputs changes what gets printed.

# ### Function 1: print_quest_header(quest_name, reward)
# Purpose
# - Prints the “top poster” of the quest.

# Parameters
# - quest_name (string): the quest title
# - reward (string): what the player earns

# ### Function 2: print_quest_details(location, danger_level)
# Purpose
# - Prints where the quest happens and how dangerous it is.
# - Uses if / elif / else to print different advice depending on danger_level.

# Parameters
# - location (string): where the mission takes place
# - danger_level (string): "low", "medium", "high" (or something else)

# ### Function 3: show_quest_board(quest_name, reward, location, danger_level)
# Purpose
# - This is the “main builder” function.
# - It doesn’t print everything itself, it calls other functions and passes the values along.

# Parameters
# - quest_name (string)
# - reward (string)
# - location (string)
# - danger_level (string)

# ## Task 3: Boss Fight - Functions with return
# What you are building are multiple functions for a boss fight.
# - roll_dice(sides)
# - calculate_damage(attack_roll)
# - apply_damage(current_hp, damage)
# - calculate_reward(base_gold, danger_level) 
# - get_battle_message(monster_name, monster_hp, gold_reward)
######################### 

def roll_dice(sides):
    roll = random.randint(1,sides)
    return roll

def calculate_damage(attack_roll):
    bonus_damage = random.randint(1,5)
    final_damage = attack_roll + bonus_damage
    if attack_roll >= 18:
        final_damage *=2
    return final_damage
def apply_damage(current_hp, damage):
    current_hp -= damage
    if current_hp <= 0:
        current_hp = 0
    return current_hp

def calculate_reward(base_gold, danger_level):
    if danger_level.lower() == "low":
        pass ## useless...
    elif danger_level.lower() == "medium":
        base_gold *= 1.5
    elif danger_level.lower() == "high":
        base_gold *=2
    else:
        base_gold *=1.2
    return base_gold
def get_battle_message(monster_name,monster_hp,gold_reward):
    if monster_hp ==0:
        print(f"You have defeated {monster_name}.")
        print(f"Gold Earned: {gold_reward}")
    else:
        print(f"{monster_name} is still alive!")
        print(f"Monster HP (Remaining): {monster_hp}")
def start_boss_fight(monster_name,monster_hp,danger_level,reward):
    print(f"=== BOSS FIGHT WITH {monster_name}, WITH {monster_hp}. DANGER LEVEL: {danger_level} REWARD: {reward} ===")
    print(f"Enemy: {monster_name}")
    print(f"Monster HP (start): {monster_hp}")

    roll_dice(6) 
 
 # Uncomment once function 1 roll_dice is done
    Turn =1
    while monster_hp > 0:
        print(f"Turn {Turn}")
        attack_roll = roll_dice(20)
        print(f"Attack roll: {attack_roll}")
        damage = calculate_damage(attack_roll)
        print(f"Damage dealt: {damage}")
    
        monster_hp = apply_damage(monster_hp, damage)
        print(f"Monster HP (after): {monster_hp}")
        Turn +=1

# # Uncomment once function 2 calculate_damage is done
# # Uncomment once function 3 apply_damage is done
    gold_reward = calculate_reward(reward, danger_level)
    get_battle_message(monster_name, monster_hp, gold_reward)
# # Uncomment once function 4 calculate_reward is done
# print(f"Gold Earned: {gold_reward}")
# # The below code is given to you. Code the functions to make it work!
# # --------------------------------
 
monster_name = "Cave Slime King"
monster_hp = 50
danger_level = "high"
reward = 100


start_boss_fight("nonchalant boss",monster_hp,danger_level,reward)
start_boss_fight("not tuff boss",67,"medium",150)
start_boss_fight("only normal boss", 100, "high", 200)
start_boss_fight("supercalifragilisticexpialidocious boss", 6000, "Extreme", 1000)

# print("=== BOSS FIGHT ===")
# print(f"Enemy: {monster_name}")
# print(f"Monster HP (start): {monster_hp}")

# roll_dice(6) 
 
#  # Uncomment once function 1 roll_dice is done
# Turn =1
# while monster_hp > 0:
#     print(f"Turn {Turn}")
#     attack_roll = roll_dice(20)
#     print(f"Attack roll: {attack_roll}")
#     damage = calculate_damage(attack_roll)
#     print(f"Damage dealt: {damage}")
    
#     monster_hp = apply_damage(monster_hp, damage)
#     print(f"Monster HP (after): {monster_hp}")
#     Turn +=1

# # # Uncomment once function 2 calculate_damage is done
# # # Uncomment once function 3 apply_damage is done
# gold_reward = calculate_reward(reward, danger_level)
# get_battle_message(monster_name, monster_hp, gold_reward)
# # # Uncomment once function 4 calculate_reward is done
# # print(f"Gold Earned: {gold_reward}")



# ### Function 1: roll_dice(sides) (Return an int)
# Purpose
# - Simulate rolling a dice.
# - Used to generate the attack_roll value for the fight.

# Input (parameter)
# - sides (int) — how many sides the dice has (e.g., 6, 20)

# Output (return)
# - an integer from 1 to sides

# ### Function 2: calculate_damage(attack_roll)
# Function Objective
# - Calculate the final damage dealt in one attack.

# Parameters Required
# - attack_roll (int): the number rolled from the dice (from function 1)

# Returns
# - int: the final damage number

# What the function must do
# - Generate weapon_bonus as a random number from 1 to 5
# - Add roll + bonus to get damage
# - If attack_roll >= 18, make it a critical hit:
# - Double the damage
# - Return the final damage. Do not print inside the function!

# How you test
# - Uncomment the “calculate_damage” lines in the demo code.
# - Run and check damage changes each time.

# ### Function 3: apply_damage(current_hp, damage)
# Function Objective
# - Update monster HP after taking damage.

# Parameters Required
# - current_hp (int): monster HP before the hit
# - damage (int): damage dealt (from function 2)

# Returns
# - int: monster HP after damage (minimum 0)

# What the function must do
# - Subtract damage from current HP
# - If the new HP is below 0, set it to 0
# - Return the new HP. Do not print inside the function

# How you test
# - Uncomment the “apply_damage” lines in the demo code.
# - Run and confirm HP never becomes negative.

# ### Function 4: calculate_reward(base_gold, danger_level)
# Function Objective
# - Calculate how much gold the player earns.

# Parameters Required
# - base_gold (int): base reward amount
# - danger_level (str): "low", "medium", "high" (or others)

# Returns
# - int: final gold reward

# What the function must do
# 1. Convert danger level to lowercase
# 2. Choose a multiplier:
# - low → 1.0
# - medium → 1.5
# - high → 2.0
# - other → 1.2
# 3. Multiply base gold by the multiplier
# 4. Return the final amount as an integer. Do not print inside the function

# How you test
# - Uncomment the “calculate_reward” line in the demo code.
# - Temporarily print the gold reward to check the value

# ### Function 5: get_battle_message(monster_name, monster_hp, gold_reward)
# Function Objective
# - Print the end-of-turn battle message.

# Parameters Required
# - monster_name (str): enemy name
# - monster_hp (int): enemy HP after damage
# - gold_reward (int): calculated gold reward

# Returns
# - None (this function prints, it does not return)

# What the function must do
# 1. Check if monster_hp is 0
# 2. If HP is 0:
# - Print a victory message
# - Include the monster name & gold earned
# 3. Else:
# - Print a “still alive” message
# - Include the monster name & remaining HP
# - Do not return anything (Discuss why!)

# How you test
# - Uncomment the “get_battle_message” lines in the demo code.
# - Make sure the main code prints the returned message.