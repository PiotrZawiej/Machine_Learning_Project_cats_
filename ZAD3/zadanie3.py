import random
# Wymiary plecaka: 10cmx20cmx10cm, 2000cm^3
# Wymiary zdobyczy: Mysz Polna 5x3x3, Mysz Domowa 7x2x2, Ślimak 3x3x3, Liść 3x2x1, Kamyk 2x2x1
# Preferencje kotów: Luna - (MP 0.4, MD 0.4, Ś 0.1, K 0.1 L 0.0), Ariana - (Ś 0.375, L 0.375, MD 0.125, MP 0.125, K 0.0), Dante (K 0.5, MD 0.2, MP 0.2, Ś 0.05 L 0.05)
#
# Metoda losująca złapaną przez kota zdobycz (Bazowo 0.2 szansy na każdą możliwą zdobycz)
def catch_prey():
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
        self.x = x
        self.y = y
        self.z = z
        self.content = dict()

    def store_prey(self):
        pass


for i in range(10):
    print(catch_prey())

