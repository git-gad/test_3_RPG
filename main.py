from input import validate_input
from sys import exit
from core import goblin, orc, player_modul
from random import randint
from game import Game

g = Game()

g.start()

g.create_player()

g.choose_random_monster()

g.difine_first_attacker()

while g.status:
    g.attack()
    g.update_status()
    g.attacker, g.victim = g.victim, g.attacker


    
    