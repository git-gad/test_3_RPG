from random import randint

professions = ['medic', 'warrior']

class Player:
    def __init__(self, name):
        self.name = name
        self.hp = 50
        self.type = 'human'
        self.speed = randint(5, 10)
        self.power = randint(5, 10)
        self.armor_rating = randint(5, 15)
        self.profession = professions[randint(0, 1)]
        if self.profession == 'medic':
            self.hp += 10
        elif self.profession == 'warrior':
            self.power += 2
    
    def speak(self):
        print(f'hi im {self.name}')

    def attack(self):
        pass
    
# p = Player('gad')

# print(p.hp, p.profession)