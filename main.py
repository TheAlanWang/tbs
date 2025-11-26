from character import Hero, Enemy
from weapon import iron_sword, short_bow
import os
import sys

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

hero = Hero("Hero", 100)

print("---- Choose weapon for hero ----\n1.Fists\n2.Iron Sword\n3.Short Bow")
choice = int(input("> "))

if choice == 1:
    hero.drop()

elif choice == 2:
    hero.equip(iron_sword)

elif choice == 3:
    hero.equip(short_bow)

else :
    print("Invalid choice, equipping iron sword.")
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
