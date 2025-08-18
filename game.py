#This is originally code that I had written in Thonny in 2022
#I'm making updates to it so that it can run with different packages

import pygame
import random
import sys

#Initialize the game
pygame.init()

#window size
WIDTH, HEIGHT = 800, 600 
#speed when jumping
BIRD_SPEED = -5
#pipe speed when moving across the screen
PIPE_SPEED = -5
#speed at which the sun crosses the screen acting as a clock
SUN_SPEED = -0.475
#speed of the clouds that pass in the background
CLOUD_SPEED = -1
#how quickly the bird drops after making its jump
GRAVITY = 0.2
#frames per second
FPS = 60

#setting up World
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Hummingbird")

#clock for game loop speed
clock = pygame.time.Clock()

#text font
font = pygame.font.SysFont(None, 36)


#load the hummingbird image
bird_img = pygame.image.load("Hummingbird.png")
#scale the hummingbird image to fit game
bird_img = pygame.transform.scale(bird_img, (60,60))
bird_rect = bird_img.get_rect(center=(100, HEIGHT //2))

#color constants

BLUE = (100,149, 239)
YELLOW = (255,255,0)
WHITE = (255,255,255)
BLACK = (0,0,0)
    
time_counter = 0
running = True
while running:
    clock.tick(60)
    screen.fill(BLUE)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            BIRD_SPEED = -5
            
    #bird's movement
    BIRD_SPEED += GRAVITY
    bird_rect.y += BIRD_SPEED
    
    #create bird
    screen.blit(bird_img, bird_rect)
    
    #timer
    time_counter += 1/60
    timer_text = font.render(f"Time: {int(time_counter)}", True, BLACK)
    screen.blit(timer_text, (10,10))
    
    #initialize the game state
    pygame.display.flip()
pygame.quit()
sys.exit()
    

