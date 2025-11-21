class HealthBar:

    remaining: str = "#"
    lost: str = "_"
    barrier: str = "|"
    colors = {
        "red": "\033[91m",
        "purple": "\033[95m",
        "blue": "\033[34m",
        "blue2": "\033[36m",
        "blue3": "\033[96m",
        "green": "\033[92m",
        "green2": "\033[32m",
        "brown": "\033[33m",
        "yellow": "\033[93m",
        "grey": "\033[37m",
        "default": "\033[0m"
    }
    
    def __init__(self,
                entity,
                length: int = 20,
                colored: bool = True,
                color: str = ""
                ) -> None:

        self.entity = entity
        self.length = length
        self.max_val = entity.max_hp
        self.cur_val = entity.hp
        self.colored = colored

        self.color = self.colors.get(color) or self.colors["default"]

    def update(self) -> None:

        self.cur_val = self.entity.hp

    def draw(self) -> None:

        remaining_bars = round(self.cur_val / self.max_val * self.length)
        lost_bars = self.length - remaining_bars

        print(f"{self.entity.name}'s HEALTH: {self.entity.hp}/{self.entity.max_hp}")

        print(f"{self.barrier}"
              f"{self.color if self.colored else ""}"
              f"{remaining_bars * self.remaining}"
              f"{lost_bars * self.lost}"
              f"{self.barrier}"
              f"{self.colors["default"] if self.colored else ""}"
        )
