import pygame
import random

pygame.init()

screen = pygame.display.set_mode((400, 400))  # Screen size
pygame.display.set_caption('Hextris')
game_over = False
clock = pygame.time.Clock()
fps = 4  # frames per second

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
# Block colors
colors = [
    (114, 0, 165),
    (255, 0, 0),
    (252, 205, 103),
    (0, 128, 255),
    (255, 0, 128),
    (245, 198, 0),
    (9, 255, 0)
]


class Block:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.type = random.randint(0, len(blocks) - 1)
        self.rotation = 0
        self.color = colors[random.randint(0, len(colors) - 1)]

    def shape(self):
        return blocks[self.type][self.rotation]


def draw_block():
    for y in range(3):
        for x in range(3):
            if y * 3 + x in block.shape():
                pygame.draw.rect(screen, block.color,
                                 [(x + block.x) * grid_size + x_gap + 1,
                                  (y + block.y) * grid_size + y_gap + 1,
                                  grid_size - 2, grid_size - 2])


def collides(nx, ny):
    collision = False
    for y in range(3):
        for x in range(3):
            if y * 3 + x in block.shape():
                if x + block.x + nx < 0 or x + block.x + nx > cols - 1:
                    collision = True
                    break
                if y + block.y + ny < 0 or y + block.y + ny > rows - 1:
                    collision = True
                    break
                if game_board[x + block.x + nx][y + block.y + ny] != (0, 0, 0):
                    collision = True
                    break
    return collision


def drop_block():
    can_drop = True
    for y in range(3):
        for x in range(3):
            if y * 3 + x in block.shape():
                if collides(0, 1):
                    can_drop = False
    if can_drop:
        block.y += 1
    else:
        for y in range(3):
            for x in range(3):
                if y * 3 + x in block.shape():
                    game_board[x + block.x][y + block.y] = block.color
    return can_drop


def side_move(dx):
    can_move = True
    for y in range(3):
        for x in range(3):
            if y * 3 + x in block.shape():
                if collides(dx, 0):
                    can_move = False
    if can_move:
        block.x += dx
    else:
        drop_block()


def rotate():
    last_rotation = block.rotation
    block.rotation = (block.rotation + 1) % len((blocks[block.type]))
    can_rotate = True
    for y in range(3):
        for x in range(3):
            if y * 3 + x in block.shape():
                if collides(0, 0):
                    can_rotate = False
    if not can_rotate:
        block.rotation = last_rotation


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


# Clear lines across grid
def find_lines():
    lines = 0
    for y in range(rows):
        empty = 0
        for x in range(cols):
            if game_board[x][y] == (0, 0, 0):
                empty += 1
        if empty == 0:
            lines += 1
            for y2 in range(y, 1, -1):
                for x2 in range(cols):
                    game_board[x2][y2] = game_board[x2][y2 - 1]
    return lines


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

score = 0

while not game_over:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
            continue
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                rotate()
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
                score += find_lines()
                block = Block(random.randint(5, cols - 5), 0)  # Randomize block placement
    pygame.display.update()

pygame.quit()
