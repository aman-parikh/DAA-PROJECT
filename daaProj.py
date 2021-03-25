import pygame
import random
import time
from maze import call

pygame.init()

#DIMENSIONS
infoObj = pygame.display.Info()
width = height = 660

#COLORS
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

#SCREEN DISPLAY
win = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()
pygame.display.set_caption('PATH FINDING VISUALIZER')
win.fill(black)
pygame.display.update()

#FONTS
font1=pygame.font.SysFont('arial',50,bold=True)
font2=pygame.font.SysFont('arial',18,bold=True)
font3=pygame.font.SysFont('arial',20,bold=True,italic=True)

def welcome():

    #images
    image = pygame.transform.scale(pygame.image.load(r'C:\Users\Isha Pranav\Desktop\miniProj\pathFinding\images\maze.jfif'), (width, height))
    win.blit(image, (0,0))

    #texts
    text = font1.render('WELCOME', True, black, white)

    text1 = font1.render('TO', True, black, white)
    text2 = font1.render('THE MAZE GAME', True, black, white)
    # text3 = font3.render('Aman', True, (0, 191, 255))
    # text4 = font3.render('Gaurav', True, (0, 191, 255))

    midx = 200
    midy = height/2 - 50

    win.blit(text, (midx, midy))
    win.blit(text1, (midx+90, midy + 100))
    win.blit(text2, (midx-80, midy + 200))
    # win.blit(text3, (midx, midy + 300))
    # win.blit(text4, (midx, midy + 400))

    pygame.display.update()

def gen():
    image = pygame.transform.scale(pygame.image.load(r'C:\Users\Isha Pranav\Desktop\miniProj\pathFinding\images\maze.jfif'), (width, height))
    win.blit(image, (0,0))

    #texts
    text = font1.render('How do you want to', 1, black, white)
    text_1 = font1.render('generate the maze ?', 1, black , white)
    text1 = font1.render('1. Manual', 1, black, white)
    text2 = font1.render('2. Automatic', 1, black, white)

    midx = 25
    midy = height/2 - 50

    win.blit(text, (midx, midy - 200))
    win.blit(text_1, (midx, midy-110))
    win.blit(text1, (midx, midy))
    win.blit(text2, (midx, midy+100))

    pygame.display.update()

def algorithms():
    image = pygame.transform.scale(pygame.image.load(r'C:\Users\Isha Pranav\Desktop\miniProj\pathFinding\images\maze.jfif'), (width, height))
    win.blit(image, (0,0))

    #texts
    text = font1.render('Algorithm ? ', 1, black, white)
    text1 = font1.render('1. Breadth First Search', 1, black, white)
    text2 = font1.render('2. Backtracking', 1, black, white)
    text3 = font1.render('3. Dijkstra Algorithm', 1, black, white)
    text4 = font1.render('4. A* Algorithm', 1, black, white)

    midx = 25
    midy = height/2 - 50

    win.blit(text, (midx, midy - 200))
    win.blit(text1, (midx, midy))
    win.blit(text2, (midx, midy+100))
    win.blit(text3, (midx, midy + 200))
    win.blit(text4, (midx, midy + 300))

    pygame.display.update()

def speed():
    image = pygame.transform.scale(pygame.image.load(r'C:\Users\Isha Pranav\Desktop\miniProj\pathFinding\images\maze.jfif'), (width, height))
    win.blit(image, (0,0))

    #texts
    text = font1.render('Visualization Speed ? ', 1, black, white)
    text1 = font1.render('1. Slow', 1, black, white)
    text2 = font1.render('2. Medium', 1, black, white)
    text3 = font1.render('3. Fast', 1, black, white)

    midx = 25
    midy = height/2 - 50

    win.blit(text, (midx, midy - 200))
    win.blit(text1, (midx, midy))
    win.blit(text2, (midx, midy+100))
    win.blit(text3, (midx, midy + 200))

    pygame.display.update()

def main():
    run = True

    welcome()

    preference = {}

    flag1 = flag2 = flag3 = flag4 = 1

    while run:
        clock.tick(60)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    run = False
                    pygame.quit()

                #user choice for generation of maze
                if event.key == pygame.K_RETURN and flag1:
                    gen()

                if flag1:
                    if event.key == pygame.K_1:
                        preference['Generation'] = 1
                        flag1 = 0
                    elif event.key == pygame.K_2:
                        preference['Generation'] = 2
                        flag1 = 0
                    continue

                #algortihm choice
                if event.key == pygame.K_RETURN and flag2:
                    algorithms()

                if flag2:
                    if event.key == pygame.K_1:
                        preference['Algo'] = 1
                        flag2 = 0
                    elif event.key == pygame.K_2:
                        preference['Algo'] = 2
                        flag2 = 0
                    elif event.key == pygame.K_3:
                        preference['Algo'] = 3
                        flag2 = 0
                    elif event.key == pygame.K_4:
                        preference['Algo'] = 4
                        flag2 = 0
                    continue

                #Speed
                if event.key == pygame.K_RETURN and flag3:
                    speed()

                if flag3:
                    if event.key == pygame.K_1:
                        preference['Speed'] = 1
                        flag3 = 0
                    elif event.key == pygame.K_2:
                        preference['Speed'] = 2
                        flag3 = 0
                    elif event.key == pygame.K_3:
                        preference['Speed'] = 3
                        flag3 = 0

                if event.key == pygame.K_s:
                    call(win, width, preference)


main()