#Welcome the player
print ("=== ESCAPE THE CASTLE===")
print ("Welcome, adventurer!")
 
#Get player name, age and character class
playerName = input("What is your name? ")
characterClass = input ("What type of adventurer are you? ")
characterAge = int(input("How old is your character? "))

#Set starting values
health = 100
gold = 20
has_key = False
inventory = []

#Display the character profile
print("\n=== CHARACTER PROFILE ===")
print(f"Name:  {playerName}")
print(f"Class: {characterClass}")
print(f"Age: {characterAge} ")
print(f"Health: {health}")
print(f"Gold: {gold}")


#Begin the story
print(f"\n{playerName}, you wake up in a dark castle.")
print("You hear footsteps approaching...")
print("Your adventure is about to begin!")

# ==========================================
# ESCAPE THE CASTLE - SCENE 1: THE CELL
# ==========================================
 #Create an inventory to store collected items
inventory = []

# Define the Cell scene
def cell():
    print("\nYou wake up in a dark castle cell.")
    print("You can see a door, a window and an old bed.")

    # Store the available choices
    choices = ["door", "window", "bed"]

    # Track whether the player has found the key
    has_key = False

    # Repeat until the player finds the key
    while has_key == False:

        # Display the remaining choices
        print("\nYou can investigate:", choices)

        choice = input("What would you like to investigate? ").lower()

        if choice not in choices:
            print("Invalid choice. Please choose an available option.")

        elif choice == "door":
            print("\nThe door is locked.")
            print("You need to find a key.")

            # Remove door from available choices
            choices.remove("door")

        elif choice == "window":
            print("\nYou look through the window.")
            print("The window is barred. You can't escape.")

            # Remove window from available choices
            choices.remove("window")

        elif choice == "bed":
            print("\nYou look underneath the bed.")
            print("You find a small Iron Key!")

            # Add key to inventory
            inventory.append("Iron Key")

            # Remove bed from available choices
            choices.remove("bed")

            # Update the variable
            has_key = True

    # Continue the story after finding the key
    print("\nYou unlock the cell door.")
    print("You step out into the corridor.")
    print(f"Your inventory: {inventory}")

# Start the scene
cell()

#==========================================
# ESCAPE THE CASTLE - SCENE 2: THE CORRIDOR
#==========================================
inventory = ["Iron Key"] 
#Introduce the scene
print("You enter a long, dark corridor.")
print("You notice an old wooden cabinet")

choice = input("Do you want to open the cabinet? (yes/no)")
if choice == "yes":
    print("You open the cabinet \nInside you find a Rusty Dagger!")
    inventory.append("Rusty Dagger")
    print("You pick up the Dagger")
elif choice == "no":
    print("You decide to leave the cabinet alone.")
print(f"\nYour inventory: {inventory}")
# cell()
#     # ==========================================
#     # ESCAPE THE CASTLE - SCENE 3: THE ROOM
#     # ==========================================
#     #guard and ghost is an argument
# def encounter(creature):
#         print("You hear footsteps approaching")
#         print(f"A {creature} appears!!")
#         print("prepare yourself")
#         if creature == "guard":
#             print("The guard draws their sword")
#         elif creature == "ghost":
#             print("The ghost floats towards you")
#         elif creature == "drauger":
#             print("The drauger wakes up and slowly walks towards you")
    
# encounter("guard")
# encounter("ghost")
# encounter("drauger")
# ==========================================
# ESCAPE THE CASTLE - SCENE 3: CORRIDOR ENCOUNTER
# ==========================================
 
import random
# Define a function to describe an encounter
def encounter(creature):
    # Different outcomes depending on the creature
    if creature == "Guard":
        print("The Guard draws their sword")
    elif creature == "Ghost":
        print("The ghost floats towards")
    elif creature == "Sphinx":
        print("the Sphinx wakes up and slowly walks towards you")
 
    print(f"A {creature} appears!!")
 
# Define the corridor scene
def corridor():
    print("You walk down a dark castle corridor.")
    print("You hear a strange noise ahead...")
    # Create a list of possible encounters
    creatures = ["Guard", "Ghost", "Sphinx"]
   
    # Randomly select a creature
    random_creature = random.choice(creatures)
 
    # Pass the chosen creature into the encounter function
    encounter(random_creature)
 
# Start the scene
corridor()