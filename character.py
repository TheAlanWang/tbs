from weapon import fists
from healthbar import HealthBar

class Character:

    def __init__(self,
                name: str,
                hp: int,
                weapon=fists
                ) -> None:
        
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.weapon = weapon
    
    def attack(self, target) -> None:

        target.hp -= self.weapon.dmg
        target.hp = max(target.hp, 0)
        target.healthbar.update()

class Hero(Character):

    def __init__(self,
                name: str,
                hp: int,
                weapon=fists
                ) -> None:
                
        super().__init__(name=name, hp=hp, weapon=weapon)

        self.default_weapon = self.weapon
        self.healthbar = HealthBar(self, color="green")

    def equip(self, weapon) -> None:

        self.weapon =  weapon

    def drop(self) -> None:
        
        self.weapon = default_weapon

class Enemy(Character):

    def __init__(self,
                name: str,
                hp: int,
                weapon=fists
                ) -> None:

        super().__init__(name=name, hp=hp, weapon=weapon)

        self.healthbar = HealthBar(self, color="red")
