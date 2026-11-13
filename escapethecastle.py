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
 
# Create a variable to track whether the player has found the key
    has_key = False
 
# Repeat while the player has not found the key
    while has_key == False:
 
# Ask the player what to investigate
        choice = input("\nInvestigate the door, window or bed? "
        ).lower()
 
        if choice == "door":
            print("The door is locked.")
            print("You need to find a key")
 
        elif choice == "window":
            print("The window is barred. You can't escape that way.")
 
        elif choice == "bed":
            print("You look underneath the bed.")
            print("You find a small Iron Key")
 
# Add the key to the inventory
            inventory.append("Iron Key")
 
# Update the variable to stop the loop
            has_key = True
 
        else:
            print("Invalid choice. Please choose 'door', 'window', or 'bed'.")
 
# Code runs once the player has found the key.
        print("\nYou unlock the cell door.")
        print("You step out into the corridor.")
        print(f"Your inventory: {inventory}")
 
 
# Start the scene
cell()
# inventory = []
 
# def cell():
#     global has_key
#     # Introduce the scene to the player
#     print("You wake up in a dark castle cell.")
#     print("You can see a door, a window and an old bed")
 
#     while has_key == False:
 
#         # Ask the player what they want to investigate
#         # .lower() converts their answer to lowercase
#         choice = input("Do you want to investigate the door, window or bed?: ").lower()
 
#         # Check whether the player chose the door
#         if choice == "door":
#             print("You walk towards the door.")
#             print("You try the handle, but is it locked.")
 
#         # Check whether the player chose the window
#         elif choice == "window":
#             print("You look through the window.")
#             print("It is too small to escape through")
 
#         # Check whether the player chose the bed
#         elif choice == "bed":
#             print("You look under the bed")
#             print("You find a small Iron Key")
#             inventory.append("Iron Key")
#             has_key = True
#         else:
#             print("You decide not to investigate")
   
#     print("\nYou unlock the cell door.")
#     print("You step out into the corridor.")
#print(f"Your inventory: {inventory}")
 
 
# cell()
#     # ==========================================
#     # ESCAPE THE CASTLE - SCENE 2: THE ROOM
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
# ESCAPE THE CASTLE - SCENE 4: CORRIDOR ENCOUNTER
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