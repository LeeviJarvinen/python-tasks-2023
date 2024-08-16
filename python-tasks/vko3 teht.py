Teht 1

"""
Testaillaan Pygame-kirjastoa.
"""

import pygame

# Alustetaan Pygame
pygame.init()

# Ruudun leveys ja korkeus
width, height = 800, 600

# Luodaan ikkuna
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pygame intro")

# Vaihdetaan ikkunan väri
screen.fill((255, 255, 255))

# Piirretään viiva
pygame.draw.line(screen, (0, 255, 0), (width / 2, 0), (width / 2, height / 2), 10)

# Piirretään ympyrä
pygame.draw.circle(screen, (0, 0, 0), (width / 2, height / 2), 25)

# Pelisilmukka
pos_list=[]
running = True
while running:

    mouse_pos = pygame.mouse.get_pos()
    # Käsitellään tapahtumat
    for event in pygame.event.get():
        # Jos painetaan ruksia, poistutaan silmukasta ja suljetaan ohjelma
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_k:
                pygame.draw.circle(screen, (255, 255, 0), (width / 2, height / 2), 25)

        # Jos painetaan vasenta nuolinäppäintä, muutetaan taustaväriä
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                screen.fill((255, 0, 0))

        if event.type == pygame.MOUSEBUTTONDOWN:
                pos_list.append(event.pos)

        for x, y in pos_list:
            pygame.draw.circle(screen, (0, 0, 0), [x, y], 25, 25)

            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                screen.fill((255, 255, 255))
                pygame.draw.line(screen, (0, 255, 0), (width / 2, 0), (width / 2, height / 2), 10)
                pygame.draw.circle(screen, (0, 0, 0), (width / 2, height / 2), 25)

    # Päivitetään kaikkien objektien paikat ja nopeudet

    # Päivitetään ruutu
    pygame.display.update()

Teht 2

"""
Testaillaan Pygame-kirjastoa.
"""

import pygame

# Fysikaaliset parametrit
g = 10
k = 1
m = 1
L = 100

# Alustetaan Pygame
pygame.init()

# Ruudun leveys ja korkeus
width, height = 400, 300

# Luodaan ikkuna
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pygame intro")

# Luodaan kello
fps = 60
clock = pygame.time.Clock()

# Alkuarvot
x_0 = width / 2
y_0 = height / 2
v_x_0 = 0
v_y_0 = 0

# Aika-askel
dt = 0.01

# Alustetaan muuttujat
x = x_0
y = y_0
v_x = v_x_0
v_y = v_y_0

# Vaihdetaan ikkunan väri
screen.fill((255, 255, 255))

# Piirretään ympyrä
pygame.draw.circle(screen, (0, 0, 0), (width / 2, height / 2), 25)

# Piirretään viiva
pygame.draw.line(screen, (0, 255, 0), (width / 2, 0), (width / 2, height / 2), 10)

# Pelisilmukka
running = True
while running:
    # Käsitellään tapahtumat
    for event in pygame.event.get():
        # Jos painetaan ruksia, poistutaan silmukasta ja suljetaan ohjelma
        if event.type == pygame.QUIT:
            running = False

        # Jos painetaan vasenta nuolinäppäintä, muutetaan taustaväriä
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                screen.fill((255, 0, 0))
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                screen.fill((255, 255, 255))

    # Päivitetään kaikkien objektien paikat ja nopeudet käyttäen Verletin yhtälöä
    a_x = 0
    a_y = g - k/m * (y - L)

    x_new = x + v_x * dt + 0.5 * a_x * dt**2
    y_new = y + v_y * dt + 0.5 * a_y * dt**2

    v_x = (x_new - x) / dt
    v_y = (y_new - y) / dt

    x = x_new
    y = y_new

    # Päivitetään ruutu
    screen.fill((255, 255, 255))
    pygame.draw.line(screen, (0, 255, 0), (x, 0), (x, y), 10)
    pygame.draw.circle(screen, (0, 0, 0), (x, y), 25)
    pygame.display.update()
    clock.tick(fps)