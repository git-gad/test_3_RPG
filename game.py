from input import validate_input
from sys import exit
from core import goblin, orc, player_modul
from random import randint

class Game:
    def start(self):
        choice = self.show_menu()
        if choice == 'exit':
            exit()
    
    def show_menu(self):
        choice = input('start or exit\n')
        choice = validate_input(choice)
        return choice
    
    def create_player(self):
        self.player = player_modul.Player('gad')
    
    def choose_random_monster(self):
        char = randint(0, 1)
        if char == 0:
            self.monster = goblin.Goblin('golum')
        else:
            self.monster = orc.Orc('worker')
    
    def battle(self):
        player_bonus_speed = self.roll_dice(6)
        monster_bonus_speed = self.roll_dice(6)
        if self.monster.speed + monster_bonus_speed < self.player.speed + player_bonus_speed:
            self.attacker, self.victim = self.player, self.monster
        else:
            self.attacker, self.victim = self.monster, self.player
        while self.player.hp > 0 and self.monster.hp > 0:    
            self.attack() 
            self.attacker, self.victim = self.victim, self.attacker
        print(f'{self.victim.name} won')
        
    def attack(self):
        self.hit_chance = self.attacker.speed + self.roll_dice(20)
        if self.hit_chance > self.victim.armor_rating:
            self.damage = self.attacker.power + self.roll_dice(6)
            if hasattr(self.attacker, 'weapon'):
                self.damage *= self.attacker.weapon.multiplier
            self.victim.hp -= self.damage
    
    def roll_dice(self, sides):
        return randint(1, sides)
    
# g = Game()

# g.create_player()

# g.choose_random_monster()

# g.battle()

# print(g.player.hp, g.monster.hp)



