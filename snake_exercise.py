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


def move_snake():
    global apple  # apple variable content the coordinates x and y of the apple on the map
    x, y = snake[0]  # X and y are the coordinates of the snake on the map
    # Complete the three point bellow, if content of direction variable equal to right, x variable will increase of one
    # if ...
    # ...
    # Complete the three point bellow, if content of direction variable equal to left, x variable will decrease of one
    # elsif ...

    # Complete the three point bellow, if content of direction variable equal to up, y variable will increase of one
    # if ...
    # ...
    # Complete the three point bellow, if content of direction variable equal to up, y variable will decrease of one
    # elsif ...

    snake.insert(0, (x, y))

    # Complete the three point bellow, if the coordinates of the snake is equal to the coordinates of the apple,
    # change the coordinates of the apple
    # if ...
        #apple = (random.randint(0, GRIDWIDTH - 1),
        #            random.randint(0, GRIDHEIGHT - 1))
    #else:
    #    del snake[-1]


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
    pygame.draw.rect(screen, (255, 0, 0), rect)


def game_over():
    draw_text(screen, "SNAKE!", 60, (255, 255, 255), WIDTH / 2, HEIGHT / 2)
    draw_text(screen, "Press a key", 48, (255, 255, 255),WIDTH / 2, HEIGHT * 3 / 4)
    pygame.display.update()
    pygame.time.wait(1000)
    waiting = True
    while waiting:
        for event in pygame.event.get():
            # Complete the three point bellow, if the type of event is equal to hey up,
            # waiting variable will pass to False
            # Complete the three point bellow, if the type of event is equal to hey quit,
            # pygame will quit the game


def event_reach(direction):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            # Complete the three point bellow, if the type of event key is equal to pygame key right or
            # the direction is different to the left in this case the content of variable direction become right
            # if ...
            # ...
            # Complete the three point bellow, if the type of event key is equal to pygame key left or
            # the direction is different to the right in this case the content of variable direction become left
            # elsif ...
            # ...
            # Complete the three point bellow, if the type of event key is equal to pygame key up or
            # the direction is different to the down in this case the content of variable direction become up
            # elsif ...
            # ...
            # Complete the three point bellow, if the type of event key is equal to pygame key down or
            # the direction is different to the up in this case the content of variable direction become down
            # elsif ...
            # ...
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
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # running = False
                pygame.quit()
        direction = event_reach()
        # updates
        move_snake()
        # Complete the three point bellow, if the snake hit a wall or itself,
        # the content of the variable running will pass to False
        # if ...

        # draw
        screen.fill((40, 40, 40))
        # draw_grid()
        draw_snake()
        draw_apple()
        draw_text(screen, str(len(snake) - 3), 32, (255, 255, 255),
                  WIDTH / 2, 10)
        pygame.display.flip()  # DO THIS LAST!

pygame.quit()
