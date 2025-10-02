game_name = "Piggy from Hell"
print(f"Welcome to {game_name}!")
print("===========================")

# Ask for the character's name 
name = input("Before we begin, what is your charcter's name? \n> ")

# Print the name
print(f"Great, {name}! Let's begin the adventure!")

# Build character stats dictionary
player = {
    "name": name,
    "health": 100,
    "coin": 0
}

# Print player stats
print(f"Character stats: {player}") 

import random

events = ["find a coin", "meet a monster", "do nothing"]
event = random.choice(events)
print(f"While exploring, you {event}!")

# Update stats
if event == "find a coin":
    player["coin"] += 1
    print(f"{player['name']} found a coin! Now has {player['coin']} coins.")
elif event == "meet a monster":
    player["health"] -= 10
    print(f"oh no! {player['name']} fought a monster and now has {player['health']} health.")
else:
    print(f"{player['name']} wandered around but nothing happened.")

# Print updated player stats 
print(f"Updated character stats: {player}")