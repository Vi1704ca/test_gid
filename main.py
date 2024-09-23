import math
import random


class Character:
    def __init__(self, name, gender, weapon, element):
        self.name = name
        self.gender = gender
        self.weapon = weapon
        self.element = element
        self.hp = 10000
        self.damage = 150

        if self.element and self.weapon:
            self.damage = 500
        elif self.element:
            self.damage = 250
        elif self.weapon:
            self.damage = 250
        else:
            self.damage = 150

    def attack(self, villain):
        if self.hp > 0:
            attack_damage = self.damage - math.tan(random.randint(1, 100000000000)) + math.sin(random.randint(1, 100000000000)) + math.cos(random.randint(1, 100000000000)) + math.pi 
            villain.hp -= attack_damage
            print(f"{self.name} атакует {villain.name} и наносит {attack_damage} урона!")
            print(f"У {villain.name} осталось {round(villain.hp)} HP.\n")
        else:
            print(f"{self.name} не может атаковать, его здоровье слишком низкое.\n")

    def is_alive(self):
        return self.hp > 0


class Scorpion(Character):
    def __init__(self):
        super().__init__("Scorpion", "male", "spear", "fire")

    def special_move(self, villain):
        if self.is_alive():
            print(f"{self.name} использует свою специальную атаку: Get Over Here!")
            special_damage = self.damage * 2
            villain.hp -= special_damage
            print(f"{self.name} наносит {round(special_damage)} урона {villain.name} своим копьём!")
            print(f"У {villain.name} осталось {round(villain.hp)} HP.\n")
        else:
            print(f"{self.name} не может использовать свою способность, его здоровье слишком низкое.\n")


class SubZero(Character):
    def __init__(self):
        super().__init__("SubZero", "male", "ice blade", "ice")

    def special_move(self, villain):
        if self.is_alive():
            print(f"{self.name} использует свою специальную атаку: Ice Freeze!")
            freeze_chance = random.randint(1, 4)
            if freeze_chance == 1:
                print(f"{villain.name} заморожен и не может двигаться!\n")
                freeze_damage = self.damage * 1.5
                villain.hp -= freeze_damage
                print(f"{self.name} наносит {round(freeze_damage)} урона {villain.name}, пока тот заморожен!")
            else:
                print(f"Заморозка не сработала, {villain.name} продолжает сражаться!\n")
        else:
            print(f"{self.name} не может использовать свою способность, его здоровье слишком низкое.\n")


scorpion = Scorpion()
subzero = SubZero()

scorpion.attack(subzero)
subzero.attack(scorpion)

scorpion.special_move(subzero)
subzero.special_move(scorpion)
