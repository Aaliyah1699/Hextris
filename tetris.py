import pygame

pygame.init()

screen = pygame.display.set_mode((500, 600))
pygame.display.set_caption('Hextris')
game_over = False


# Grid
def draw_grid(rows, cols, grid_size):
    # Create grid and place on screen
    for y in range(rows):
        for x in range(cols):
            pygame.draw.rect(screen, (100, 100, 100), [x * grid_size, y * grid_size, grid_size, grid_size], 1)


while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    screen.fill((0, 0, 0))
    # Grid
    draw_grid(10, 10, 30)

    pygame.display.update()

pygame.quit()
