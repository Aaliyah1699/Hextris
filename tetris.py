import pygame

pygame.init()

screen = pygame.display.set_mode((600, 600))  # Screen size
pygame.display.set_caption('Hextris')
game_over = False

# Blocks shape
blocks = [
    [[1, 4, 7], [3, 4, 5]],  # Vertical & Horizontal
    [[1, 3, 4, 5, 7]],  # Cross
    [[0, 1, 4, 5], [1, 3, 4, 6]],  # Z shape pt 1
    [[1, 2, 3, 4], [0, 3, 4, 7]],  # Z shape pt2
    [[0, 1, 3, 6], [0, 1, 2, 5], [2, 5, 7, 8], [3, 6, 7, 8]],  # L shape pt1
    [[1, 2, 5, 8], [5, 6, 7, 8], [0, 3, 6, 7], [0, 1, 2, 3]],  # L shape pt2
    [[4, 6, 7, 8], [0, 3, 4, 6], [0, 1, 2, 4], [2, 4, 5, 8]]  # T shape
]


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
