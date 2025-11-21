class Weapon:

    def __init__(self,
            name: str,
            wtype: str,
            dmg: int,
            val: int
            ) -> None:
        
        self.name = name
        self.wtype = wtype
        self.dmg = dmg
        self.val = val
    
iron_sword = Weapon("Iron Sword", "sharp", 5, 10)

short_bow = Weapon("Short Bow", "ranged", 4, 8)

fists = Weapon("Fists", "blunt", 2, 0)
