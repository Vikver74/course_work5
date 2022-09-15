import random
from marshmallow_dataclass import dataclass


@dataclass
class Weapon:
    id: int
    name: str
    min_damage: float
    max_damage: float
    stamina_per_hit: float

    def count_damage(self) -> float:
        return random.uniform(self.min_damage, self.max_damage)


@dataclass
class Armor:
    id: int
    name: str
    defence: float
    stamina_per_turn: float
