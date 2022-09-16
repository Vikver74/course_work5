from flask import session

from classes.person import Enemy, Hero
from classes.unit import unit


def choose_unit_hero(request) -> None:
    session['hero_name'] = request.form.get('name')
    session['hero_base_class_person'] = int(request.form.get('unit_class'))
    session['hero_weapon'] = int(request.form.get('weapon'))
    session['hero_armor'] = int(request.form.get('armor'))


def choose_unit_enemy(request) -> None:
    session['enemy_name'] = request.form.get('name')
    session['enemy_base_class_person'] = int(request.form.get('unit_class'))
    session['enemy_weapon'] = int(request.form.get('weapon'))
    session['enemy_armor'] = int(request.form.get('armor'))


def create_hero() -> Hero:
    name: str = session['hero_name']
    base_class_person = unit.classes_person[session['hero_base_class_person']]
    weapon = unit.weapons[session['hero_weapon']]
    armor = unit.armors[session['hero_armor']]
    return Hero(name=name, base_class_person=base_class_person, weapon=weapon, armor=armor)


def create_enemy() -> Enemy:
    name: str = session['enemy_name']
    base_class_person = unit.classes_person[session['enemy_base_class_person']]
    weapon = unit.weapons[session['enemy_weapon']]
    armor = unit.armors[session['enemy_armor']]
    return Enemy(name=name, base_class_person=base_class_person, weapon=weapon, armor=armor)

