from __future__ import annotations
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from person import BasePerson


class Skill(ABC):
    user = None
    target = None

    @property
    @abstractmethod
    def name(self) -> str:
        raise NotImplementedError

    @property
    @abstractmethod
    def damage(self) -> float:
        raise NotImplementedError

    @property
    @abstractmethod
    def required_stamina(self):
        raise NotImplementedError

    @abstractmethod
    def skill_effect(self) -> str:
        raise NotImplementedError

    def use_skill(self, user: BasePerson, target: BasePerson) -> str:
        self.user = user
        self.target = target
        result: str = self.skill_effect()
        self.user.stamina_points = round((self.user.stamina_points - self.user.base_class_person.skill.required_stamina), 2)
        return result


class FierceKick(Skill):
    def __init__(self, name: str = 'Свирепый пинок', damage: int = 12, required_stamina: int = 6):
        self._name = name
        self._damage = damage
        self._required_stamina = required_stamina

    @property
    def name(self) -> str:
        return self._name

    @property
    def damage(self) -> int:
        return self._damage

    @property
    def required_stamina(self) -> float:
        return self._required_stamina

    def skill_effect(self) -> str:
        skill_attack: float = self.damage * self.user.base_class_person.attack
        skill_defense: float = self.target.armor.defence * self.target.base_class_person.armor
        skill_damage: float = round((skill_attack - skill_defense), 2)

        if skill_damage > 0:
            self.target.health_points = self._decrease_stamina_target(skill_damage)
            result: str = f'{self.user.name} использует {self.user.base_class_person.skill.name} и наносит {skill_damage} урона сопернику.'
        else:
            result: str = f'{self.user.name}, используя {self.user.base_class_person.skill.name}, наносит удар, но {self.target.armor.name} соперника его останавливает.'
        return result

    def _decrease_stamina_target(self, skill_damage) -> float:
        result: float = round((self.target.health_points - skill_damage), 2)
        if result > 0:
            return result
        else:
            return 0


class PowerfulInjection(Skill):
    def __init__(self, name: str = 'Мощный укол', damage: int = 15, required_stamina: int = 5):
        self._name = name
        self._damage = damage
        self._required_stamina = required_stamina

    @property
    def name(self) -> str:
        return self._name

    @property
    def damage(self) -> int:
        return self._damage

    @property
    def required_stamina(self) -> float:
        return self._required_stamina

    def skill_effect(self) -> str:
        skill_attack: float = self.damage * self.user.base_class_person.attack
        skill_defense: float = self.target.armor.defence * self.target.base_class_person.armor
        skill_damage: float = round((skill_attack - skill_defense), 2)

        if skill_damage > 0:
            self.target.health_points = self._decrease_stamina_target(skill_damage)
            result: str = f'{self.user.name} использует {self.user.base_class_person.skill.name} и наносит {skill_damage} урона сопернику.'
        else:
            result: str = f'{self.user.name}, используя {self.user.base_class_person.skill.name}, наносит удар, но {self.target.armor.name} соперника его останавливает.'
        return result

    def _decrease_stamina_target(self, skill_damage) -> float:
        result: float = round((self.target.health_points - skill_damage), 2)
        if result > 0:
            return result
        else:
            return 0


fierce_kick = FierceKick()
powerful_injection = PowerfulInjection()
