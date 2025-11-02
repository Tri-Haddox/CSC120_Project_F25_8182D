game_name = "Zombie Break"
print(f"Welcome to {game_name}!")
print("===========================")

# Ask for the character's name 
name = "Tester"

# Print the name
print(f"Great, {name}! Let's begin the adventure!")

# Build character stats dictionary
player = {
    "name": name,
    "health": 100,
    "coin": 0,
    "x": 0,
    "y": 0
}

# Print player stats
print(f"Character stats: {player}") 

import random

events = ["find a coin", "meet a monster", "do nothing"]

def check_event():
    global events, player
    event = random.choice(events)

if events == "find a coin":
    player["coin"] += 1
elif events == "meet a monster":
    player["health"] -= 10
else:
    pass

