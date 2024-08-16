"""
Ruudussa liikkuvia ympyröitä.
"""

import math
import pygame

class Particle:
    def __init__(self, m=1, x=0, y=0, v_x=0, v_y=0, colour=pygame.Color("orange"), radius=0.5):
        self.m = m
        self.x = x
        self.y = y
        self.v_x = v_x
        self.v_y = v_y
        self.a_x = 0
        self.a_y = 0


        self.colour = colour
        self.radius = radius

    def draw(self, env):
        centre = env.env_to_screen(self.x, self.y)
        size = self.radius * env.scale
        pygame.draw.circle(env.screen, self.colour, centre, size)


class Environment:
    def __init__(self, screen):
        self.screen = screen

        self.width_pixels = self.screen.get_width()
        self.height_pixels = self.screen.get_height()
        self.width = 10
        self.scale = self.width_pixels / self.width
        self.height = self.height_pixels / self.scale

        self.g = 10
        self.particles = []
        self.dt = 0.01

    def update(self):
        for p in self.particles:
            if p.y > 0:
                p.a_y = -self.g
            else:
                p.a_y = self.g
                
            p.v = math.sqrt(p.v_x**2 * p.v_y**2)
            if p.v > 3:
                p.colour = pygame.Color("purple")


            p.x += self.dt * p.v_x
            p.y += self.dt * p.v_y

            p.v_x += self.dt * p.a_x
            p.v_y += self.dt * p.a_y

    def draw(self):
        self.screen.fill(pygame.Color("white"))
        for p in self.particles:
            p.draw(self)

    def env_to_screen(self, x, y):
        x_screen = self.scale * x + self.width_pixels / 2
        y_screen = -self.scale * y + self.height_pixels / 2

        return x_screen, y_screen

    def screen_to_env(self, x_screen, y_screen):
        x = (x_screen - self.width_pixels / 2) / self.scale
        y = -(y_screen - self.height_pixels / 2) / self.scale

        return x, y

    def add_particle(self, x, y, v_x=0, v_y=0, m=1, radius=0.5):
        self.particles.append(Particle(m=m, x=x, y=y, v_x=v_x, v_y=v_y, radius=radius))



# Alustetaan Pygame
pygame.init()

# Ruudun leveys ja korkeus
width, height = 1200, 1000

# Luodaan ikkuna
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Simulaatio")

# Luodaan kello
fps = 60
clock = pygame.time.Clock()

# Luodaan ympäristö
env = Environment(screen)

# Pelisilmukka
running = True
while running:
    # Käsitellään tapahtumat
    for event in pygame.event.get():
        # Jos painetaan ruksia, poistutaan silmukasta ja suljetaan ohjelma
        if event.type == pygame.QUIT:
            running = False

        # Jos klikataan hiirellä, lisätään kappale (vasen näppäin == 1)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x_screen_start, y_screen_start = event.pos
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            x_screen_end, y_screen_end = event.pos
            v_x = (x_screen_start - x_screen_end) * 0.03
            v_y = -(y_screen_start - y_screen_end) * 0.03
            x, y = env.screen_to_env(x_screen_start, y_screen_start)
            env.add_particle(x, y, v_x, v_y)

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            x_screen, y_screen = event.pos
            x, y = env.screen_to_env(x_screen, y_screen)
            env.add_particle(x, y, m=2, radius=0.25)


    # Päivitetään kaikkien objektien paikat ja nopeudet
    env.update()

    # Päivitetään ruutu
    env.draw()
    pygame.display.update()
    clock.tick(fps)