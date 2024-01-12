import random
from collections import Counter
# Wymiary plecaka: 10cmx20cmx10cm, 2000cm^3
# Wymiary zdobyczy: Mysz Polna 5x3x3, Mysz Domowa 7x2x2, Ślimak 3x3x3, Liść 3x2x1, Kamyk 2x2x1
# Preferencje kotów: Luna - (MP 0.4, MD 0.4, Ś 0.1, K 0.1 L 0.0), Ariana - (Ś 0.375, L 0.375, MD 0.125, MP 0.125, K 0.0), Dante (K 0.5, MD 0.2, MP 0.2, Ś 0.05 L 0.05)
#
prey_size = {'Field Mouse': 45, 'House Mouse': 28, 'Snail': 27, 'Leaf': 6, 'Rock': 4}
luna_preferences = {'Field Mouse': 0.4, 'House Mouse': 0.4, 'Snail': 0, 'Leaf': 0.0, 'Rock': 0.1}
ariana_preferences = {'Field Mouse': 0.125, 'House Mouse': 0.125, 'Snail': 0.375, 'Leaf': 0.375, 'Rock': 0}
dante_preferences = {'Field Mouse': 0.2, 'House Mouse': 0.2, 'Snail': 0.05, 'Leaf': 0.05, 'Rock': 0.5}


class Cat:
    name = ''
    def __init__(self, name):
        match name:
            case ('Luna'):
                self.name = 'Luna'
            case ('Ariana'):
                self.name = 'Ariana'
            case ('Dante'):
                self.name = 'Dante'
            case _:
                self.name = -1
    def select_prey(self):
        selection = random.randint(1, 10)
        match selection:
            case (1 | 2):
                return 'Field Mouse'
            case (3 | 4):
                return 'House Mouse'
            case (5 | 6):
                return 'Slug'
            case (7 | 8):
                return 'Leaf'
            case (9 | 10):
                return 'Rock'
            case _:
                return -1

class Backpack:

    def __init__(self, x=10, y=20, z=10):
        contents = []
        volume = 0
        max_volume = x*y*z
        is_full = False

    def store_prey(self, prey):
        if self.volume + prey_size[prey] <= self.max_volume:
            self.contents.append(prey)
            self.volume += prey_size[prey]
            print(f"Stored {prey}.")
        else:
            print("The backpack is full!")


