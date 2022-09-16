from classes.person import BasePerson
from constants import STAMINA_PER_TURN


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


class Arena(metaclass=Singleton):
    hero: BasePerson
    enemy: BasePerson
    is_play = False

    def start_game(self, hero: BasePerson, enemy: BasePerson) -> None:
        self.hero = hero
        self.enemy = enemy
        self.is_play = True

    def hit(self) -> str:
        result_hero: str = self.hero.hit(self.enemy)
        if self._check_health(self.enemy) <= 0:
            result: str = result_hero + f' {self.hero.name} победил!'
            self.is_play = False
            return result

        result_enemy: str = self.enemy.hit(self.hero)
        if self._check_health(self.hero) <= 0:
            result: str = result_enemy + f' {self.enemy.name} победил!'
            self.is_play = False
            return result

        self._restore_stamina(self.hero)
        self._restore_stamina(self.enemy)
        result: str = result_hero + ' ' + result_enemy
        return result

    def use_skill(self) -> str:
        if self.hero.is_used_skill:
            return f'{self.hero.name} уже использовал {self.hero.base_class_person.skill.name}'

        result_hero: str = self.hero.use_skill(self.enemy)
        if self._check_health(self.enemy) <= 0:
            result: str = result_hero + f' {self.hero.name} победил!'
            self.is_play = False
            return result

        result_enemy: str = self.enemy.hit(self.hero)
        if self._check_health(self.hero) <= 0:
            result: str = result_enemy + f' {self.enemy.name} победил!'
            self.is_play = False
            return result

        self._restore_stamina(self.hero)
        self._restore_stamina(self.enemy)
        result: str = result_hero + ' ' + result_enemy
        return result

    def skip_move(self) -> str:
        result: str = self.enemy.hit(self.hero)
        if self._check_health(self.hero) <= 0:
            self.is_play = False
            result += f' {self.enemy.name} победил!'
        self._restore_stamina(self.hero)
        self._restore_stamina(self.enemy)
        return result

    @staticmethod
    def _check_health(player: BasePerson) -> float:
        return player.health_points

    @staticmethod
    def _restore_stamina(player: BasePerson) -> None:
        player.stamina_points = round((player.stamina_points + STAMINA_PER_TURN * player.base_class_person.stamina), 2)
        if player.stamina_points > player.base_class_person.max_stamina:
            player.stamina_points = player.base_class_person.max_stamina
