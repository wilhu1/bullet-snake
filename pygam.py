import pygame
import random
pygame.init()
timer = pygame.time.Clock()

# Setting up window
screen = pygame.display.set_mode([500, 500])

red = (255, 0, 0)

# Function to check if cursor collides with food
def is_colliding(circle_pos, mouse_pos, radius):
    distance = ((mouse_pos[0] - circle_pos[0]) ** 2 + (mouse_pos[1] - circle_pos[1]) ** 2) ** 0.5
    return distance < radius

# Initial position for food
food = (random.randint(30, 470), random.randint(30, 470))

# Run until user prompts to quit
run = True
while run:
    timer.tick(60)
    screen.fill((0, 0, 0))
    pygame.mouse.set_visible(0)
    mouse_position = pygame.mouse.get_pos()
    
    # Collision check and repositioning food
    if is_colliding(food, mouse_position, 10 + 20):  # cursor radius + food radius
        food = (random.randint(30, 470), random.randint(30, 470))

    # Draw cursor and food
    pygame.draw.circle(screen, red, mouse_position, 10)
    pygame.draw.circle(screen, red, food, 20)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()

pygame.quit()