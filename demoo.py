import os
import streamlit as st
from dotenv import load_dotenv
from google import genai
import random
 
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
 
client = genai.Client(api_key=api_key) if api_key else None
 
MODEL_NAME = "gemini-3.5-flash-lite"

def roll_dice():
    return random.randint(1,6)

dice = roll_dice()

print(dice)
st.write("You need a 4, 5 or 6 to cross a narrow bridge.")
if st.button("Attempt the bridge"):
    roll = roll_dice()
    st.write(f"You rolled {roll}.")
    if roll == 6:
        st.success("Excellent! A perfect crossing!")
    elif roll == 5:
        st.success("You did it! Cross the bridge")
    elif roll == 4:
        st.success("A win is a win, you can cross")
    elif roll == 3:
        st.error("Not on my watch! Better luck next time")
    elif roll == 2:
        st.error("That's too bad, no crossing for you")
    else:
        st.error("Is that the best you can do?")
if "water_ml" not in st.session_state:
    st.session_state.water_ml = 600
 
max_capacity = 1000
water_left, water_right = st.columns(2)
with water_left:
    if st.button("💧 Refill 250 ml"):
        st.session_state.water_ml = min(max_capacity, st.session_state.water_ml + 250)
with water_right:
    if st.button("🥤 Drink 250 ml"):
        st.session_state.water_ml = max(0, st.session_state.water_ml - 250)
 
st.write(f"Bottle: {st.session_state.water_ml}/{max_capacity} ml")
 
if "basic_shopping_list" not in st.session_state:
    st.session_state.basic_shopping_list = []
 
def add_item(item):
    if item not in st.session_state.basic_shopping_list:
                    st.session_state.basic_shopping_list.append(item)
 
def has_item(item):
     return item in st.session_state.basic_shopping_list
 
def remove_item(item):
     if item in st.session_state.basic_shopping_list:
                         st.session_state.basic_shopping_list.remove(item)
 
 
 
shop_options = ["Rope", "Bread", "Apples", "Water Bottle"]
 
for item in shop_options:
    buy_col, check_col, return_col = st.columns(3)
    with buy_col:
        if st.button(f"Buy {item}"):
            add_item(item)
    with check_col:
        if st.button(f"Check {item}"):
            if has_item(item):
                st.success(f"{item} is on the list.")
            else:
                st.warning(f"{item} is not on the list.")
    with return_col:
        if st.button(f"Put back {item}"):
            remove_item(item)
 
st.write("Current shopping list:", st.session_state.basic_shopping_list)
 
 
st.header("🌊 River crossing")
st.write("You can use Rope bought in the function-based shop above. A Rope adds +2 to your dice roll.")
st.write("A total of 4 or higher succeeds. A failed crossing costs 1 energy point.")
 
# This state is only needed for the river challenge, so it starts here.
if "river_energy" not in st.session_state:
    st.session_state.river_energy = 5
 
def take_damage(amount):
     st.session_state.river_energy = max(0, st.session_state.river_energy - amount)
 
def chance_encounter(success_number, bonus_item=""):
     roll = roll_dice()
     bonus = 0
     if bonus_item != "" and has_item(bonus_item):
        bonus = 2
     total = roll + bonus
     st.write(f"Dice: {roll} | Equipment bonus: {bonus} | Total: {total}")#
     if total >= success_number:
          st.success("Success! You crossed the river safely.")
     else:
          take_damage(1)
          st.error("Failure! You fall into the river and lose 1 energy.")
 
if st.session_state.river_energy > 0:
     if st.button("🌊 Attempt the river crossing"):
          chance_encounter(success_number=4, bonus_item="Rope")
else:
    st.error("You have no energy left. Reset to try again.")
 
if st.button("🔄 Reset river energy"):
     st.session_state.river_energy = 5
     st.rerun()
 
st.write(f"Energy: {st.session_state.river_energy}/5")
#Make the following changes to your code:
#increase the amount of energy lost if the player rolls a 1 or 2
#add an energy drink to the shop that increases energy by 1 if bought
#ensure energy does not go above 5
#add a second scenario of climbing a steep mountain path. Success requires a roll of 5 or more. Owning climbing boots gives players a + 1 modifier to their roll.