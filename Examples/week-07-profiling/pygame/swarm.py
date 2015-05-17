import math
import pygame
import random
import sys

# from meliae import scanner
# scanner.dump_all_objects("meliae.dump") # you can pass a file-handle if you prefer

NUMBER_OF_SPHERES = 150

size = width, height = 800, 600
pygame.init()
black = 0, 0, 0
screen = pygame.display.set_mode(size)

class Sphere(object):
    def __init__(self):
        self.ball = pygame.image.load("ball.gif")
        self.x = random.random() * width
        self.y = random.random() * height
        vx = 150*(random.random() - .5)
        vy = 150*(random.random() - .5)
        self.v = [vx, vy]

    def update_v(self, other ):
        """update v with gravitational force of other"""
        d = math.sqrt( (self.x - other.x)**2 + (self.y - other.y)**2)
        v = ((other.x - self.x), (other.y - self.y))
        f = map(lambda x: 200 * x / (d*d), v)
        self.v = [self.v[0] + f[0], self.v[1] + f[1]]

    def move(self, speed):
        self.x = self.x + self.v[0] * speed
        self.y = self.y + self.v[1] * speed

    def draw(self):
        screen.blit(self.ball, (self.x, self.y))

class Sun(Sphere):
    def __init__(self):
        self.ball = pygame.image.load("sun.gif")
        self.x = width / 2.0
        self.y = height / 2.0
        self.v = [0,0]

if __name__ == "__main__":

    sun = Sun()

    titlebar = pygame.Rect(0,0,200, 100)
    clock = pygame.time.Clock()

    spheres = [Sphere() for i in xrange(NUMBER_OF_SPHERES)]
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT \
                or event.type == pygame.KEYDOWN:
                sys.exit()
        screen.fill(black)

        dt = clock.tick(40)
        fps = clock.get_fps()
        speed = 1 / float(dt)

        for sphere in spheres:
            sphere.update_v(sun)
            sphere.move(speed)
            sphere.draw()

        sun.draw()

        pygame.draw.rect(screen, (0,0,0), titlebar)
        # screen.blit(label, (10, 10))

        pygame.display.flip()

