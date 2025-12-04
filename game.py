import random

class player:
    def __init__(self):
        self.name = "Tester"
        self.health = 100
        self.coin = 0
        self.x = 0
        self.y = 0
 
    def move(self, direction, map_size):
        if direction == 'w' and self.x > 0:
            self.x -= 1
        elif direction == 'a' and self.y > 0:
            self.y -= 1
        elif direction == 's' and self.x < map_size - 1:
            self.x += 1
        elif direction == 'd' and self.y < map_size - 1:
            self.y += 1
        else:
            print("You cannot move that way!") 
       
class GameMap:
    def __init__(self):
        self.size = 9
        
    def draw(self, player):
        print("=" * 25)
        for i in range(self.size):
            for j in range(self.size):
                if i == player.x and j == player.y:
                    print("C", end="  ")  # Character
                elif i == self.size - 1 and j == self.size - 1:
                    print("M", end="  ")  # Monster or goal
                else:
                    print(".", end="  ")
            print()

        print("=" * 25)
        print(f"Health: {player.health}")
        print("-" * 25)
        print(f"Coin: {player.coin}")
        print("=" * 25)
       
        
class Game:
    def __init__(self):
        self.game_name = "Zombie Break"
        self.name = "Tester"
        self.events = ["find a coin", "meet a monster", "do nothing"]
        self.player = player()
        self.map = GameMap()
       
    def check_event(self):
        event = random.choice(self.events)
         
        if event == "find a coin":
            self.player.coin += 1
        elif event == "meet a monster":
            self.player.health -= 10

         
    def play(self):
      print(f"Welcome to {self.game_name}!")
      print("===========================")
      print(f"Great, {self.player.name}! Let's begin the adventure!")
      print(f"Character stats: {{'name': '{self.player.name}', 'health': {self.player.health}, 'coin': {self.player.coin}, 'x': {self.player.x}, 'y': {self.player.y}}}")
      
      direction = None
      self.map.draw(self.player)
      
      direction = input("Your next move (w/a/s/d/q): ").lower()
      
      while direction != "q":
        self.player.move(direction, self.map.size)
        
        if self.player.x == self.map.size - 1 and self.player.y == self.map.size - 1:
            print("Congratulations! You reach the gate for next level.")
            break

        self.check_event()
        self.map.draw(self.player)
        direction = input("Your next move (w/a/s/d/q): ").lower() 

if __name__ == "__main__":
    Game().play()