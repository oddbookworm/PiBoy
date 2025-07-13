import pygame

pygame.init()

window = pygame.Window("PiBoy", (480, 320), (0, 0), fullscreen_desktop = True)
screen = window.get_surface()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or \
            (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False

    screen.fill((0, 0, 0))  # Clear the screen with black
    window.flip()  # Update the display
