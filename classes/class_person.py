from marshmallow_dataclass import dataclass
from classes.skill import Skill, fierce_kick, powerful_injection


@dataclass
class BaseClassPerson:
    name: str
    max_health: float
    max_stamina: float
    attack: float
    armor: float
    stamina: float
    skill: Skill


warrior_class = BaseClassPerson(name='Воин', max_health=60, max_stamina=30, attack=0.8, armor=1.2, stamina=0.9, skill=fierce_kick)
thief_class = BaseClassPerson(name='Вор', max_health=50, max_stamina=25, attack=1.5, armor=1, stamina=1.2, skill=powerful_injection)

classes_person_dict = {1: warrior_class,
                       2: thief_class}

