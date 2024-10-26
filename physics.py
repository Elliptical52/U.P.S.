import math

particles = []

## CONSTANTS
GLUE = 25
####

class Particle:
    def __init__(self, x=0, y=0):
        particles.append(self)
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0



    def update(self):
        self.x += self.vx
        self.y += self.vy

    def shove(self, target, velocity):
        dx = target.x - self.x
        dy = target.y - self.y
        velocity = 1/velocity

        self.vx += dx/velocity
        self.vy += dy/velocity

e = Particle(100, 100)
f = Particle()


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


def cool(particles):
    for particle in particles:
        for target in particles:
            if particle!=target:
                particle.shove(target, .5)

def glue(particles):
    for particle in particles:
        for target in particles:
            if particle!=target:
                dx = particle.x - target.x
                dy = particle.y - target.y
                distance = math.sqrt(dx**2 + dy**2)

                if distance <= GLUE:
                    bond(particle, target)