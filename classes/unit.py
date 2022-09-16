import json
from typing import Dict
import os.path

import marshmallow_dataclass
from marshmallow_dataclass import dataclass

from classes.class_person import BaseClassPerson, classes_person_dict
from classes.equipment import Armor, Weapon
from constants import PATH_TO_EQUIPMENTS, FILE_NAME_EQUIPMENTS


@dataclass
class Unit:
    classes_person: Dict[int, BaseClassPerson]
    weapons: Dict[int, Weapon]
    armors: Dict[int, Armor]


WeaponSchema = marshmallow_dataclass.class_schema(Weapon)
ArmorSchema = marshmallow_dataclass.class_schema(Armor)


def create_unit() -> Unit:
    if not os.path.exists(os.path.join(PATH_TO_EQUIPMENTS, FILE_NAME_EQUIPMENTS)):
        raise FileNotFoundError

    with open(os.path.join(PATH_TO_EQUIPMENTS, FILE_NAME_EQUIPMENTS), encoding='utf-8') as file:
        equipments = json.load(file)
        weapon_dict = {}
        armor_dict = {}

        count_id: int = 1
        for record in equipments['weapons']:
            weapon_obj = WeaponSchema().load(record)
            weapon_dict[count_id] = weapon_obj
            count_id += 1

        count_id = 1
        for record in equipments['armors']:
            armor_obj = ArmorSchema().load(record)
            armor_dict[count_id] = armor_obj
            count_id += 1
    return Unit(classes_person_dict, weapon_dict, armor_dict)


unit = create_unit()
