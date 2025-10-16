import pygame
from crt_filter import CrtFilter

pygame.init()

# Request an OpenGL 3.3 Core Profile context BEFORE creating the window
pygame.display.gl_set_attribute(pygame.GL_CONTEXT_MAJOR_VERSION, 3)
pygame.display.gl_set_attribute(pygame.GL_CONTEXT_MINOR_VERSION, 3)
pygame.display.gl_set_attribute(
    pygame.GL_CONTEXT_PROFILE_MASK, pygame.GL_CONTEXT_PROFILE_CORE
)

WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.OPENGL | pygame.DOUBLEBUF)
clock = pygame.time.Clock()

crt = CrtFilter(screen)
frame = pygame.Surface((WIDTH, HEIGHT))

running = True
while running:
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            running = False

    frame.fill((0, 40, 20))
    pygame.draw.circle(frame, (0, 255, 80), (WIDTH // 2, HEIGHT // 2), 100)
    crt.draw(frame)
    clock.tick(60)

pygame.quit()
