# item classes

from random import randint


class Items:
    def __init__(self):
        self.isConsumable = False
        self.isWeapon = False

        super(Items, self).__init__()

    def use(person):
        pass


class HealthPotion(Items):
    def __init__(self):
        self.isConsumable = True
        self.isWeapon = False

        self.value = randint(100, 200)

        super(HealthPotion, self).__init__()

    def use(person, self):
        person.healthPoints += self.value


class StrengthPotion(Items):
    def __init__(self):
        self.isConsumable = True
        self.isWeapon = False

        self.value = randint(10, 20)

        super(HealthPotion, self).__init__()

    def use(person, self):
        person.attackPower += self.value


class Weapon(Items):
    def __init__(self):
        self.isConsumable = False
        self.isWeapon = True

        self.power = randint(20, 50)
