import pygame
import random

pygame.init()

screen = pygame.display.set_mode((600, 600))  # Screen size
pygame.display.set_caption('Hextris')
game_over = False
clock = pygame.time.Clock()
fps = 5  # frames per second

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


class Block:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.type = random.randint(0, 6)
        self.rotation = 0

    def shape(self):
        return blocks[self.type][self.rotation]


def draw_block():
    for y in range(3):
        for x in range(3):
            if y * 3 + x in block.shape():
                pygame.draw.rect(screen, (255, 255, 255),
                                 [(x + block.x) * grid_size + x_gap + 1,
                                  (y + block.y) * grid_size + y_gap + 1,
                                  grid_size - 2, grid_size - 2])


def drop_block():
    can_drop = True
    for y in range(3):
        for x in range(3):
            if y * 3 + x in block.shape():
                if block.y + y >= rows - 1:
                    can_drop = False
    if can_drop:
        block.y += 1
    else:
        for y in range(3):
            for x in range(3):
                if y * 3 + x in block.shape():
                    game_board[x + block.x][y + block.y] = (9, 255, 0)
    return can_drop


def side_move(dx):
    can_move = True
    for y in range(3):
        for x in range(3):
            if y * 3 + x in block.shape():
                if x + block.x >= cols - 1 and dx == 1:
                    can_move = False
                elif x + block.x < 1 and dx == -1:
                    can_move = False
    if can_move:
        block.x += dx
    else:
        drop_block()


# Grid
def draw_grid():  # Passing in (cols, rows, grid_size, x_gap, y_gap)
    # Create grid and place on screen
    for y in range(rows):
        for x in range(cols):
            pygame.draw.rect(screen, (100, 100, 100),
                             [x * grid_size + x_gap, y * grid_size + y_gap, grid_size, grid_size], 1)
            # Draw blocks on top of grid
            if game_board[x][y] != (0, 0, 0):
                pygame.draw.rect(screen, game_board[x][y],
                                 [x * grid_size + x_gap, y * grid_size + y_gap + 1, grid_size - 1, grid_size - 1])


# Have grid spread over screen size
grid_size = 30
cols = screen.get_width() // grid_size
rows = screen.get_height() // grid_size
x_gap = (screen.get_width() - cols * grid_size) // 2
y_gap = (screen.get_height() - rows * grid_size) // 2

block = Block((cols - 1) // 2, 0)

# Game Board (initialize)
game_board = []
for i in range(cols):
    new_col = []
    for j in range(rows):
        new_col.append((0, 0, 0))
    game_board.append(new_col)

while not game_over:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
            continue
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            side_move(-1)
        if event.key == pygame.K_RIGHT:
            side_move(1)

    screen.fill((0, 0, 0))
    # Functions
    draw_grid()  # Passing in (cols, rows, grid_size, x_gap, y_gap)
    if block is not None:
        draw_block()  # Display blocks
        if event.type != pygame.KEYDOWN:
            if not drop_block():
                block = Block(random.randint(5, cols - 5), 0)  # Randomize block placement
    pygame.display.update()

pygame.quit()
