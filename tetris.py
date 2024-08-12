import pygame

pygame.init()

screen = pygame.display.set_mode((600, 600))  # Screen size
pygame.display.set_caption('Hextris')
game_over = False


# Grid
def draw_grid():  # Passing in (cols, rows, grid_size, x_gap, y_gap)
    # Create grid and place on screen
    for y in range(rows):
        for x in range(cols):
            pygame.draw.rect(screen, (100, 100, 100),
                             [x * grid_size + x_gap, y * grid_size + y_gap, grid_size, grid_size], 1)


# Have grid spread over screen size
grid_size = 30
cols = screen.get_width() // grid_size
rows = screen.get_height() // grid_size
x_gap = (screen.get_width() - cols * grid_size) // 2
y_gap = (screen.get_height() - rows * grid_size) // 2

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    screen.fill((0, 0, 0))
    # Grid
    draw_grid()  # Passing in (cols, rows, grid_size, x_gap, y_gap)

    pygame.display.update()

pygame.quit()
