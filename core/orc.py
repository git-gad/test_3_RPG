from random import randint, choice
from core.weapons import weapons

class Orc:
    def __init__(self, name):
        self.name = name
        self.hp = 50
        self.type = 'orc'
        self.speed = randint(0, 5)
        self.power = randint(0, 15)
        self.armor_rating = randint(2, 8)
        self.weapon = choice(weapons)()
        
    def speak(self):
        print(f'orc {self.name} ready to work')

    def attack(self):
        pass
    
