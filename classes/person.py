from abc import ABC, abstractmethod
from classes.class_person import BaseClassPerson
from classes.equipment import Armor, Weapon
import random


class BasePerson(ABC):
    def __init__(self, name: str, base_class_person: BaseClassPerson, weapon: Weapon, armor: Armor):
        self.name: str = name
        self.base_class_person: BaseClassPerson = base_class_person
        self._health_points: float = base_class_person.max_health
        self._stamina_points: float = base_class_person.max_stamina
        self.weapon: Weapon = weapon
        self.armor: Armor = armor
        self._is_used_skill: bool = False

    @property
    def health_points(self) -> float:
        return self._health_points

    @health_points.setter
    def health_points(self, points: float) -> None:
        self._health_points = points

    @property
    def stamina_points(self) -> float:
        return self._stamina_points

    @stamina_points.setter
    def stamina_points(self, points: float) -> None:
        self._stamina_points = points

    @property
    def is_used_skill(self) -> bool:
        return self._is_used_skill

    @abstractmethod
    def hit(self, target) -> str:
        raise NotImplementedError

    @abstractmethod
    def use_skill(self, target) -> str:
        raise NotImplementedError

    def _check_is_used_skill(self) -> bool:
        return self.is_used_skill

    def _check_stamina(self) -> bool:
        return self.stamina_points > self.weapon.stamina_per_hit

    def _hit_effect(self, target) -> str:
        hit_attack: float = self.base_class_person.attack * self.weapon.count_damage()
        hit_defense: float = target.base_class_person.armor * target.armor.defence
        hit_damage: float = round((hit_attack - hit_defense), 2)

        if hit_damage > 0:
            target.health_points = round((target.health_points - hit_damage), 2)
            result: str = f'{self.name}, используя {self.weapon.name}, пробивает {target.armor.name} соперника и наносит {hit_damage} урона.'
        else:
            result: str = f'{self.name}, используя {self.weapon.name}, наносит удар, но {target.armor.name} соперника его останавливает.'

        target.stamina_points = self._decrease_stamina_per_turn(target)
        self.stamina_points = self._decrease_stamina_per_hit()
        return result

    def _decrease_stamina_per_hit(self) -> float:
        result: float = round((self.stamina_points - self.weapon.stamina_per_hit), 2)
        if result > 0:
            return result
        else:
            return 0

    @staticmethod
    def _decrease_stamina_per_turn(target) -> float:
        result: float = round((target.stamina_points - target.armor.stamina_per_turn), 2)
        if result > 0:
            return result
        else:
            return 0


class Hero(BasePerson):
    def hit(self, target: BasePerson) -> str:
        if not self._check_stamina():
            return f'{self.name} попытался использовать {self.weapon.name}, но у него не хватило выносливости.'
        return self._hit_effect(target)

    def use_skill(self, target: BasePerson) -> str:
        if self._check_is_used_skill():
            return f'{self.name} уже использовал {self.base_class_person.skill.name}'
        if not self._check_stamina():
            return f'{self.name} попытался использовать {self.base_class_person.skill.name}, но у него не хватило выносливости.'

        result: str = self.base_class_person.skill.use_skill(self, target)
        self._is_used_skill = True
        return result


class Enemy(BasePerson):
    def hit(self, target: BasePerson) -> str:
        if not self._check_is_used_skill() and self._check_stamina():
            if random.randint(0, 10) == 3:
                return self.use_skill(target)
        if not self._check_stamina():
            return f'{self.name} попытался использовать {self.weapon.name}, но у него не хватило выносливости.'
        return self._hit_effect(target)

    def use_skill(self, target) -> str:
        result: str = self.base_class_person.skill.use_skill(self, target)
        self._is_used_skill = True
        return result



