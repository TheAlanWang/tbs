from character import Hero, Enemy
from weapon import fists, iron_sword, short_bow
import os
import sys

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

hero = Hero("Hero", 100)

print("-----choose your hero weapon----- \n 1.Fists \n 2.Iron Sword \n 3.Short Bow ")
choice = input( )

if choice == "2":
    hero.equip(iron_sword)

elif choice == "1":
    hero.equip(fists)

elif choice == "3":
    hero.equip(short_bow)

else :
    print("invalid choice ,Equipping Iron sword")
    hero.equip(iron_sword)


    
enemy = Enemy("Enemy", 100)

while True:
    clear_screen()

    hero.attack(enemy)
    enemy.attack(hero)
        
    hero.healthbar.draw()
    enemy.healthbar.draw()
        
    print("\nPress Enter to fight or Ctrl+C to exit.")
        
    try:
        input()
    except KeyboardInterrupt:
        print("\nExiting.")
        sys.exit(0)
