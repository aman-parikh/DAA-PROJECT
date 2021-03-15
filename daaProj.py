import pygame
import random
import time

pygame.init()

#DIMENSIONS
infoObject = pygame.display.Info()
width = infoObject.current_w
height = infoObject.current_h

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
font1=pygame.font.SysFont('arial',80,bold=True)
font2=pygame.font.SysFont('arial',18,bold=True)
font3=pygame.font.SysFont('arial',60,bold=True,italic=True)

def welcome():

    #images
    image = pygame.transform.scale(pygame.image.load(r'C:\Users\Isha Pranav\Desktop\miniProj\pathFinding\images\maze.jfif'), (width, height))
    win.blit(image, (0,0))

    #texts
    text = font1.render('WELCOME TO THE MAZE GAME', 1, black, white)

    # text1 = font3.render('made by:', True, white)
    # text2 = font3.render('Pranav', True, (0, 191, 255))
    # text3 = font3.render('Aman', True, (0, 191, 255))
    # text4 = font3.render('Gaurav', True, (0, 191, 255))

    midx = 25
    midy = height/2 - 100

    win.blit(text, (midx, midy))
    # win.blit(text1, (midx, midy + 100))
    # win.blit(text2, (midx, midy + 200))
    # win.blit(text3, (midx, midy + 300))
    # win.blit(text4, (midx, midy + 400))

    pygame.display.update()

def main():
    run = True

    welcome()

    while run:
        clock.tick(60)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    run = False
                    pygame.quit()

main()