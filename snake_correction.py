# https://gist.github.com/cbscribe
# To install pygame, open command prompt:
# pip install pygame

import pygame
import random

WIDTH = 800
HEIGHT = 600
FPS = 25
CELLSIZE = 25
GRIDWIDTH = WIDTH / CELLSIZE
GRIDHEIGHT = HEIGHT / CELLSIZE

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

font_name = pygame.font.match_font("Arial")


def draw_text(surface, text, size, color, x, y):
    font = pygame.font.Font(font_name, size)
    text_img = font.render(text, True, color)
    text_rect = text_img.get_rect(midtop=(x, y))
    surface.blit(text_img, text_rect)


def rand_color():
    r = random.randrange(256)
    g = random.randrange(256)
    b = random.randrange(256)
    return (r, g, b)


def move_snake():
    global apple
    x, y = snake[0]
    if direction == "r":
        x += 1
    if direction == "l":
        x -= 1
    if direction == "u":
        y -= 1
    if direction == "d":
        y += 1
    snake.insert(0, (x, y))
    if snake[0] == apple:
        apple = (random.randint(0, GRIDWIDTH - 1),
                 random.randint(0, GRIDHEIGHT - 1))
    else:
        del snake[-1]


def hit_wall():
    x, y = snake[0]
    if x in [-1, GRIDWIDTH] or y in [-1, GRIDHEIGHT]:
        return True


def hit_self():
    if snake[0] in snake[1:]:
        return True


def draw_grid():
    for x in range(0, WIDTH, CELLSIZE):
        pygame.draw.line(screen, (80, 80, 80), (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, CELLSIZE):
        pygame.draw.line(screen, (80, 80, 80), (0, y), (WIDTH, y))


def draw_snake():
    for segment in snake:
        x, y = segment
        x *= CELLSIZE
        y *= CELLSIZE
        rect1 = pygame.Rect(x, y, CELLSIZE, CELLSIZE)
        pygame.draw.rect(screen, (0, 155, 0), rect1)
        rect2 = pygame.Rect(x + 4, y + 4, CELLSIZE - 8, CELLSIZE - 8)
        pygame.draw.rect(screen, (0, 255, 0), rect2)


def draw_apple():
    x, y = apple
    x *= CELLSIZE
    y *= CELLSIZE
    rect = pygame.Rect(x, y, CELLSIZE, CELLSIZE)
    #pygame.draw.rect(screen, rand_color(), rect)
    pygame.draw.rect(screen, (255, 0, 0), rect)


def game_over():
    draw_text(screen, "SNAKE!", 60, (255, 255, 255),
              WIDTH / 2, HEIGHT / 2)
    draw_text(screen, "Press a key", 48, (255, 255, 255),
              WIDTH / 2, HEIGHT * 3 / 4)
    pygame.display.update()
    pygame.time.wait(1000)
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                waiting = False
            if event.type == pygame.QUIT:
                pygame.quit()


def event_reach(direction):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and direction != "l":
                direction = "r"
            if event.key == pygame.K_LEFT and direction != "r":
                direction = "l"
            if event.key == pygame.K_UP and direction != "d":
                direction = "u"
            if event.key == pygame.K_DOWN and direction != "u":
                direction = "d"
    return direction

while True:
    game_over()
    snake = [(20, 15), (19, 15), (18, 15)]
    direction = "r"
    apple = (random.randint(0, GRIDWIDTH - 1),
             random.randint(0, GRIDHEIGHT - 1))

    running = True
    while running:
        clock.tick(FPS)
        # events
        direction = event_reach(direction)
        # updates
        move_snake()
        if hit_wall() or hit_self():
            running = False
        # draw
        screen.fill((40, 40, 40))
        draw_grid()
        draw_snake()
        draw_apple()
        draw_text(screen, str(len(snake) - 3), 32, (255, 255, 255),
                  WIDTH / 2, 10)
        pygame.display.flip()  # DO THIS LAST!

pygame.quit()
