import pygame
import random
pygame.init()
timer = pygame.time.Clock()


screen = pygame.display.set_mode([500, 500])
white = (255, 255, 255)
green = (0, 255, 0)

def is_colliding(circle_pos, mouse_pos, radius):
    distance = ((mouse_pos[0] - circle_pos[0]) ** 2 + (mouse_pos[1] - circle_pos[1]) ** 2) ** 0.5
    return distance < radius

food = (random.randint(30, 470), random.randint(30,470))


run = True
while run:
    timer.tick(60)
    screen.fill((0, 0, 0))
    pygame.mouse.set_visible(0)
    mouse_position = pygame.mouse.get_pos()

    
    if is_colliding(food, mouse_position, 10 + 20):  # cursor radius + food radius
        food = (random.randint(30, 470), random.randint(30, 470))

    
    pygame.draw.circle(screen, white, mouse_position, 10)
    pygame.draw.circle(screen, green, food, 20)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()
pygame.quit()