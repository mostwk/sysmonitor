import pygame
import random

x = pygame.init()
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 200, 0)
display_width = 800
display_height = 600
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Slither")


clock = pygame.time.Clock()
block_size = 10
FPS = 20

font = pygame.font.SysFont(None, 25)


def snake( block_sizem, snakelist):
    for XnY in snakelist:
        pygame.draw.rect(gameDisplay, green, [XnY[0], XnY[1], block_size, block_size])


def message_to_screen(msg, color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [display_width / 4, display_height / 2])


def gameLoop():
    gameExit = False
    gameOver = False
    lead_x = display_width / 2
    lead_y = display_height / 2

    lead_x_change = 0
    lead_y_change = 0

    snakeList = []
    snakeLength = 1

    randAppleX = random.randrange(0, display_width - block_size, 10)
    randAppleY = random.randrange(0, display_height - block_size, 10)

    while not gameExit:
        while gameOver:
            gameDisplay.fill(white)
            message_to_screen("Game Over, press C to play again or Q to quit", black)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -block_size
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = block_size
                elif event.key == pygame.K_UP:
                    lead_y_change = -block_size
                elif event.key == pygame.K_DOWN:
                    lead_y_change = block_size
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    lead_x_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    lead_y_change = 0

        if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
            gameOver = True
        lead_x += lead_x_change
        lead_y += lead_y_change
        if lead_x == randAppleX and lead_y == randAppleY:
            randAppleX = random.randrange(0, display_width - block_size, 10)
            randAppleY = random.randrange(0, display_height - block_size, 10)
            snakeLength += 1
        gameDisplay.fill(white)
        pygame.draw.rect(gameDisplay, red, [randAppleX, randAppleY, block_size, block_size])

        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)
        if len(snakeList) > snakeLength:
            del snakeList[0]
        if snakeHead in snakeList[:-1]:
            gameOver = True
        snake(block_size, snakeList)
        pygame.display.update()
        clock.tick(FPS)
    pygame.quit()
    quit()


gameLoop()
