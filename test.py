import pygame
from crt_filter import CrtFilter

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.OPENGL | pygame.DOUBLEBUF)
clock = pygame.time.Clock()

# Create the CRT postprocessor
crt = CrtFilter(screen)

# Create a normal pygame surface to draw your game
frame = pygame.Surface((WIDTH, HEIGHT))

running = True
t = 0
while running:
    dt = clock.tick(60) / 1000
    t += dt

    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            running = False

    # Draw your regular 2D stuff here
    frame.fill((0, 50, 20))
    pygame.draw.circle(frame, (0, 255, 100), (int(WIDTH/2 + 100 * pygame.math.sin(t)), HEIGHT//2), 80)
    pygame.draw.rect(frame, (255, 160, 40), (300, 400, 200, 100))
    pygame.draw.line(frame, (255, 255, 255), (0, 0), (WIDTH, HEIGHT), 2)

    # Apply CRT postprocess
    crt.draw(frame)
