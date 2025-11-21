import os
from character import  Hero, Enemy
from weapon import short_bow, iron_sword

hero = Hero("Hero", 100)
hero.equip(iron_sword)

enemy = Enemy("Enemy", 100)

while True:
    os.system("clear")

    hero.attack(enemy)
    enemy.attack(hero)

    hero.healthbar.draw()
    enemy.healthbar.draw()

    input()
