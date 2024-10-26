class Particle:
    pass

class Pilk(Particle):
    def __init__(self):
        super().__init__()
        self.stability = 0
        self.strength = .5

class Egg(Particle):
    def __init__(self):
        super().__init__()
        self.stability = .25
        self.strength = 0

def glue(particles):
    for particle in particles:
        for target in particles:
            if particle!=target:
                print(f'{particle} ----> {target}')
glue([1,2,3,4,5,6])