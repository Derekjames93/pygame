import pygame
import random
#Intiailize pygame
pygame.init()
#Create screen (width,height)
screen = pygame.display.set_mode((1000,700))
# Make clock var for framerate
clock = pygame.time.Clock()
# Title and Icon
pygame.display.set_caption("Shaman King!")
icon = pygame.image.load('ai.png')
pygame.display.set_icon(icon)
gelato = pygame.image.load('gelato.png')
# Player
player_x = 100
player_y = 350
x= 50
y = 425
width = 40
height = 60
vel = 5
player_img = pygame.image.load('yoh.png')
playerx_change = 0
playery_change = 0
left = False
right = False
walkCount = 0
# Function for walking animation
walkRight = [pygame.image.load('yoh.png'),pygame.image.load('yohmove1.png'), pygame.image.load('yohmove2.png'), pygame.image.load('yohmove3.png'),
pygame.image.load('yohmove4.png'),pygame.image.load('yohmove5.png'), pygame.image.load('yohmove6.png'), pygame.image.load('yohmove7.png'),
]
walkLeft  = [pygame.image.load('yoh.png'),pygame.image.load('yohmove1.png'), pygame.image.load('yohmove2.png'), pygame.image.load('yohmove3.png'),
pygame.image.load('yohmove4.png'),pygame.image.load('yohmove5.png'), pygame.image.load('yohmove6.png'), pygame.image.load('yohmove7.png'),
]
def player(x,y):
    screen.blit(player_img,(x,y))  #This Draws the player onto the screen with .blit
#Enemy
enemy_img = pygame.image.load('yoh.png')
enemy_x = random.randint(500,1000)
enemy_y = random.randint(0,700)
enemyX_change = 0
enemyY_change = 0
def enemy(x,y):
    screen.blit(enemy_img,(x,y))
# Make a draw function
def redDraw():
    global walkCount
    # screen.fill((0,0,0))
    screen.blit(gelato, (0,0))
    player(player_x,player_y)
    if walkCount + 1 >= 70:
        walkCount = 0
    if left:
        screen.blit(walkLeft[walkCount//3]), (player_x,player_y)
        walkCount += 1
    elif right:
        screen.blit(walkRight[walkCount//3]), (player_x,player_y)
        walkCount += 1
    else:
        player(player_x,player_y)
    pygame.display.update()
#Game loop
running  = True
while running :
    clock.tick(70)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running  = False
        #if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN: # KEYDOWN CHECKS FOR A KEY BEING PRESSED
            if event.key == pygame.K_LEFT:
                playerx_change = -5
                enemyX_change = 0
                walkLeft = True   # Set variable for walk left to true and right to false so it wont move
                walkRight = False
            else:
                walkLeft = False
                walkRight = False
                walkCount = 0
            if event.key == pygame.K_UP:
                playery_change = -5
                enemyY_change = 0
            if event.key == pygame.K_DOWN:
                playery_change = 5
                enemyY_change = 0
            if event.key == pygame.K_RIGHT:
                playerx_change = 5
                enemyX_change = 0
                walkLeft = True
                walkRight = False
            else:
                walkLeft = False
                walkRight = False
                walkCount = 0
        if event.type == pygame.KEYUP:  # THIS IS FOR WHEN KEY IS BEING RELEASED
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerx_change = 0
                enemyX_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playery_change = 0
                enemyY_change = 0
        walkCount
    player_y += playery_change
    player_x += playerx_change
    enemy_x += enemyX_change
    enemy_y += enemyY_change
    #Player boundary
    if player_x <= 0 :
        player_x = 0
    elif player_x >= 875:
        player_x = 875
    if player_y <= 0 :
        player_y = 0
    elif player_y >= 580:
        player_y = 580
    #Enemy Boundary
    if enemy_x <= 0 :
        enemy_x = 0
    elif enemy_x >= 875:
        enemy_x = 875
    if enemy_y <= 0 :
        enemy_y = 0
    elif enemy_y >= 580:
        enemy_y = 580
    redDraw()
       # Call player after screen otherwise the screen will be drawn over player
    #enemy(enemy_x,enemy_y)


















