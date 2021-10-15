# The character of the player

from random import randint


class Character():
    def __init__(self):
        self.weapon = None
        self.hands_ON = True

        # This is a modifable stat
        self.healthPoints = randint(800, 1200)
        self.attackPower = 10

        self.agility = 50
        self.accuracy = 100

        self.effect = None

        super(Character, self).__init__()

    def equipWeapon(self, weapon):
        self.weapon = weapon

    def attack(self, weapon):
        if weapon is None:
            return self.attackPower*randint(1, 5)
        else:
            return (self.attackPower+self.weapon.power)*randint(1, 5)
