from random import randint, choice
from core.weapons import weapons

class Goblin:
    def __init__(self, name):
        self.name = name
        self.hp = self.max_hp = 20
        self.type = 'goblin'
        self.speed = randint(5, 10)
        self.power = randint(5, 10)
        self.armor_rating = 1
        self.weapon = choice(weapons)()
                
    def speak(self):
        print(f'my treasure')

    def attack(self):
        pass
    
    def run_away(self):
        pass
    

    