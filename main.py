from character import Hero, Enemy
from weapon import IRON_SWORD
import os

hero = Hero("Hero", 100)
hero.equip(IRON_SWORD)

enemy = Enemy("Enemy", 100)

while True:
    # change 'clear' to 'cls' on windows systems
    os.system("clear")
    hero.attack(enemy)
    enemy.attack(hero)
    hero.healthbar.draw()
    enemy.healthbar.draw()
    input()
