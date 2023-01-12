import pygame
import sys
import time
import random

#init pygame
pygame.init()

#initialize variables
width = 800
height = 600
fps = 10

#colors
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
darkBlue = (0,0,128)
white = (255,255,255)
black = (0,0,0)
pink = (255,200,200)

#set game window
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('Snake Game')
clock = pygame.time.Clock()

#snake start position
snakePos = [100,50]
snakeBody = [[100,50],[90,50],[80,50]]

#food position
foodPos = [random.randrange(1,width/10)*10,random.randrange(1,height/10)*10]
foodSpawn = True

#game over
gameOver = False

#direction
direction = 'RIGHT'
changeto = direction

#score
score = 0

#main game loop
while not gameOver:

    #check for user input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                changeto = 'RIGHT'
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                changeto = 'LEFT'
            if event.key == pygame.K_UP or event.key == ord('w'):
                changeto = 'UP'
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                changeto = 'DOWN'
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))

    #validate direction
    if changeto == 'RIGHT' and not direction == 'LEFT':
        direction = 'RIGHT'
    if changeto == 'LEFT' and not direction == 'RIGHT':
        direction = 'LEFT'
    if changeto == 'UP' and not direction == 'DOWN':
        direction = 'UP'
    if changeto == 'DOWN' and not direction == 'UP':
        direction = 'DOWN'

    #update snake position [x,y]
    if direction == 'RIGHT':
        snakePos[0] += 10
    if direction == 'LEFT':
        snakePos[0] -= 10
    if direction == 'UP':
        snakePos[1] -= 10
    if direction == 'DOWN':
        snakePos[1] += 10

    #snake body
    snakeBody.insert(0,list(snakePos))
    if snakePos[0] == foodPos[0] and snakePos[1] == foodPos[1]:
        score += 1
        foodSpawn = False
    else:
        snakeBody.pop()

    #food spawn
    if foodSpawn == False:
        foodPos = [random.randrange(1,width/10)*10,random.randrange(1,height/10)*10]
    foodSpawn = True

    #background
    screen.fill(black)

    #draw snake
    for pos in snakeBody:
        pygame.draw.rect(screen,green,pygame.Rect(pos[0],pos[1],10,10))

    #draw food
    pygame.draw.rect(screen,white,pygame.Rect(foodPos[0],foodPos[1],10,10))

    #game over
    if snakePos[0] > width or snakePos[0] < 0:
        gameOver = True
    if snakePos[1] > height or snakePos[1] < 0:
        gameOver = True
    for block in snakeBody[1:]:
        if snakePos[0] == block[0] and snakePos[1] == block[1]:
            gameOver = True

    #show score
    showScore = "Score : " + str(score)
    label = pygame.font.SysFont("arial",20)
    text = label.render(showScore,1,white)
    screen.blit(text,(width-200,height-20))

    pygame.display.flip()

    clock.tick(fps)

pygame.quit()
sys.exit()