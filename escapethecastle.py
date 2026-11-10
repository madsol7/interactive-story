#Welcome the player
print ("=== ESCAPE THE CASTLE===")
print ("Welcome, adventurer!")
 
#Get player name, age and character class
playerName = input("What is your name?")
characterClass = input ("What type of adventurer are you?")
characterAge = int(input("How old is your character"))

#Set starting values
health = 100
gold = 20 
hasKey = False
 
#Display the character profileprint("\n=== CHARACTER PROFILE ===")
print (f"Name: (playerName)")
print (f"Class: (characterclass)")
print(f"Age: (characterAge) ")
print(f"Health: (health)")
print (f"Gold: (gold)")
print (f"Has Key: (hasKey)")

#Begin the story
print (f"in(playerName), you wake up in a dark castle.")
print("You hear footsteps approaching...")
print("Your adventure is about to begin!")