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
hasKey = False
inventory = []

#Display the character profile
print("\n=== CHARACTER PROFILE ===")
print(f"Name:  {playerName}")
print(f"Class: {characterClass}")
print(f"Age: {characterAge} ")
print(f"Health: {health}")
print(f"Gold: {gold}")
print(f"Has a Key: {hasKey}")

#Begin the story
print(f"\n{playerName}, you wake up in a dark castle.")
print("You hear footsteps approaching...")
print("Your adventure is about to begin!")

# ==========================================
# ESCAPE THE CASTLE - SCENE 1: THE CELL
# ==========================================
Inventory = []
def cell():
    global hasKey
    # Introduce the scene to the player
    print("You wake up in a dark castle cell.")
    print("You can see a door, a window and an old bed")

    while hasKey == False
    # Ask the player what they want to investigate
    # .lower() converts their answer to lowercase
    choice = input("Do you want to investigate the door, window or bed? ").lower()

    # Check whether the player chose the door
    if choice == "door":
        print("You walk towards the door.")
        print("You try the handle, but it is locked")
    # Check whether the player chose the window
    elif choice == "window":
        print("You look through the window")
        print("It is too small to escape through")
    # Check whether the player chose the bed
    elif choice == "bed":
        print("You look under the bed")
        print("You find a small iron key")
        hasKey = True
        inventory.append("Iron key")
    else:
        print("You decide not to investigate")

    # Introduce the scene
    print("You enter a long, dark corridor")
    print("You notice an old wooden cabinet")
    choice = input("Do you open the cabinet? yes/no: ").lower()

    if choice == "yes":
        print("You open the cabinet")
        print("Inside, you find a Rusty Dagger!")
        inventory.append("Rusty Dagger")
        print("You pick up the dagger")
    elif choice == "no":
        print("You leave the cabinet closed.")

    print(f"\nYour Inventory: {inventory}")
    cell()
    # ==========================================
    # ESCAPE THE CASTLE - SCENE 3: THE ROOM
    # ==========================================
    #guard and ghost is an argument
    def encounter(creature):
        print("You hear footsteps approaching")
        print(f"A {creature} appears!!")
        print("prepare yourself")
        if creature == "guard":
            print("The guard draws their sword")
        elif creature == "ghost":
            print("The ghost floats towards you")
        elif creature == "drauger":
            print("The drauger wakes up and slowly walks towards you")
        

    encounter("guard")
    encounter("ghost")
    encounter("drauger")
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