import enum
import random


class Suit(enum.Enum):
    spades = 7 # пики
    hearts = 5 # черви
    diamonds = 3 # бубны
    clubs = 2 # трефы

    def __str__(self):
        return self.name


class Value(enum.Enum):
    two = 11
    three = 13
    four = 17
    five = 19
    six = 23
    seven = 29
    eight = 31
    nine = 37
    ten = 41
    jack = 43
    queen = 47
    king = 53
    ace = 59

    def __str__(self):
        return self.name


class Card:
    def __init__(self, generation_mode="none"):
        if generation_mode == "none":
            self.suit = None
            self.value = None
        elif generation_mode == "random":
            self.suit = random.choice(list(Suit))
            self.value = random.choice(list(Value))

    def __str__(self):
        str_state = '(' + str(self.suit) + ' ' + str(self.value) + ')'

        return str_state

    def code(self):
        if self.suit is not None and self.value is not None:
            code = int(self.suit.value)*int(self.value.value)
        else:
            code = 0
        return code