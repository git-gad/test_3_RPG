from input import validate_input
from sys import exit
from core import goblin, orc, player_modul
from random import randint
from game import Game

g = Game()

g.start()

g.create_player()

g.choose_random_monster()

g.battle()

# print(g.player.hp, g.monster.hp)

    
    