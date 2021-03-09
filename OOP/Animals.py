class Animal:

    def __init__(self, species, paws):
        self.species = species
        self.paws = paws

class Mammals(Animal):
    pass

class Insects(Animal):
    
    def __init__(self, species, paws, antennas):
        super().__init__(species, paws)
        self.antennas = antennas

class Birds(Animal):
    
    def __init__(self, species, paws):
        super().__init__(species, paws)

    def can_fly(self, flying):
        if flying == 0:
            return "Can't fly"
        elif flying == 1:
            return 'Can fly'
        else:
            return 'Invalid. Valid values are 0 and 1'



an_1 = Mammals('Cat', 4)
an_2 = Insects('Ladybug', 6, 2)
an_3 = Birds('Duck', 2)
print(an_3.can_fly(1))

