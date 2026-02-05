# ## Task 1: List of planets
# **Task: Create a list of 8 planets in the solar system**

# **Task 1a**:
# Create a list of 8 planets in the solar system.
# (Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune)

# **Task 1b**:
# You have conquered Mars, **rename** Mars to a name of
# your liking

# **Task 1c**:
# 1. You have decided Pluto is a planet again, **add** Pluto
#    into the list
# 2. You created an artificial planet between Earth and
#    Mars called "Lalaland". **Insert** the planet in
#    correctly into the list.

# **Task 1d**:
# You launched a war againts Jupiter and destroyed it,
# **delete** Jupiter from the list
# ---------------------------------------------------------------------------
planets = [
    "Mercury",  ## index 0
    "Venus",    ## index 1
    "Earth",    ## index 2
    "Mars",     ## index 3
    "Jupiter",  ## index 4
    "Saturn",   ## index 5
    "Uranus",   ## index 6
    "Neptune"   ## index 7
]
# print(planets[3])
# print("BREAKING NEWS - MARS REPLACED WITH GENG WOON PLANET")
planets[3] = "Geng Woon Planet"
# print(planets[3])
# planets.insert(3,"Moon"(3 is the index u wana add, moon is str))
# planets.append("Moon") - add at the end
# print("hi Pluto")
planets.append("Pluto")
# print(planets)
# print("lets add Lalaland!")
planets.insert(3,"Lalaland")
# print("Hi Lalaland!")
# print(planets)
# print("BYE JUPITER")
planets.pop(5)
# print(planets)
# planets.pop(#) removes
# planets.delete[3]
# for i in range(len(planets)):
#     print(planets[i])

# 1. Write a for loop and print out all the names of the
#    planets
# 2. If name == "Earth", print "<planet name> : this is
#    my home"
# 3. If name == "Mars" (or changed name), print
#    "<planet name> : I conquered this"
# 4. If name == "Lalaland", print
#    "<planet name> : I created this"
# for i in range(len(planets)):
#     if planets[i] == "Earth":
#         print(planets[i] + ": dis is my home")
#     elif planets[i] == "Geng Woon Planet":
#         print(planets[i] + ": I conquered Mars(now Geng Woon Land :D)")
#     elif planets[i] == "Lalaland":
#         print(planets[i] + ": i created this")
#     else:
#         print(planets[i])
## Task 3: Flight Round the Globe
# Task: Write a program to keep track of the countries you
# are visiting.

# 1. Use a while loop to ask the user what country they
#    would like to visit.
# 2. Add the country into a list
# 3. If the user types "end", exit the loop
# 4. Print all the countries in the list in this format.
#    "I would like to visit Germany"
#    "I would like to visit Japan"
#    ... 
# countries = []
# while True:
#     BL = input("what country would you like to visit(answer 'end' to exit loop)\n")
#     if BL == "end":
#         break
#     countries.append(BL)
# for i in range(len(countries)):
#     print("I would like to visit " + countries[i])


# ## Task 4: Restaurant Menu
# **Task 4a**:
# Write a program to create a menu for a new
# restaurant

# 1. Using a while loop, ask the user (the restaurant manager)
#    to input food items
# 2. Add each food item into the menu list
# 3. End the loop when the user types "end"

# **Task 4b**:
# Based on the list created by the restaurant manager, do
# the following:

# 1. Imagine a customer has come in, ask the customer what
#    would they like to eat?
# 2. If the food is in the list, say "Yes we sell that,
#    please have a seat"
# 3. else, say "Sorry, please go next door, bye."
menu = []
while True:
    additems = input("What should we add to our menu(print end to exit)\n")
    if additems == "end":
        break
    menu.append(additems)
print("We sell:" + str(menu))
order = input("What would you like to eat? One Item Only.\n")

if order in menu:
    print("Yes, we sell that here.")
else:
    print("Sorry, please go next door, bye.")
    