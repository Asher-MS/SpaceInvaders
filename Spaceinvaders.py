import pygame
import random
import time

pygame.init() #intialize the pygame module

screen=pygame.display.set_mode((800,600)) #create the window

pygame.display.set_caption("Space Invaders")
icon=pygame.image.load("MainIcon.png")  #enconuterd ERROR While SElecting ICon Error Edit:Solved by making the file 32*32
pygame.display.set_icon(icon)




#Player
playerimg=pygame.image.load("Game_character.png")
playerX=370
playerY=480 
playerX_C=0
playerY_C=0

#enemy
enemyimage=pygame.image.load("Enemy.png")
enemyX=random.randint(0,800)
enemyY=random.randint(50,150)
enemyX_C=0.1
enemyY_C=0

enemy1image=pygame.image.load("Enemy.png")
enemy1X=random.randint(0,800)
enemy1Y=random.randint(50,150)
enemy1X_C=0.1
enemy1Y_C=0


enemy2image=pygame.image.load("Enemy.png")
enemy2X=random.randint(0,800)
enemy2Y=random.randint(50,150)
enemy2X_C=0.1
enemy2Y_C=0


bulletimage=pygame.image.load("Bullet.png")
bulletX=playerX
bulletY=playerY
bulletX_C=1
bulletY_C=-0.5


explsionimg=pygame.image.load("explosion.png")



def playerplacer(x,y):
    screen.blit(playerimg,(x,y))

def enemyplacer(x,y):
    screen.blit(enemyimage,(x,y))

def enemy1placer(x,y):
    screen.blit(enemy1image,(x,y))

def enemy2placer(x,y):
    screen.blit(enemy2image,(x,y))

def bulletplacer(x,y):
    screen.blit(bulletimage,(x,y))

def explosionplacer(x,y):
    screen.blit(explsionimg,(x,y))


#Window
running=True
bulleton=False
score=0

#Game Loop
while running:
    
    
    
    
    
    
    for event in pygame.event.get():      #loops through all the events 
        #print(event)
        if(event.type==pygame.QUIT):     #listens for the pressing of the close Button
            running=False
   
        if(event.type==pygame.KEYDOWN):        #checks for a key atroke
            if(event.key==pygame.K_LEFT):
                #print("left Key is pressed")
                playerX_C=-0.5
                
         
            if(event.key==pygame.K_RIGHT):
                #print("Right Key is Pressed")
                playerX_C=0.5
              

                
        if(event.type==pygame.KEYUP):
            #print("Key has been released")
            playerX_C=0

        
        if(playerX>=736):
            playerX=736
        if(playerX<=0):
            playerX=0


        if(event.type==pygame.KEYDOWN):
            if(event.key==pygame.K_SPACE):
                bulleton=True  
                #print("SPACE") 
                bulletX=playerX
                bulletY=playerY
        
       
         
    
        
    screen.fill((0,0,40)) #colouring the screen
    playerplacer(playerX,playerY)
    playerX+=playerX_C
     


    if(enemyX>736):
        enemyX_C=-0.1
    if(enemyX<0):
        enemyX_C=0.1
    
    if(enemy1X>736):
        enemy1X_C=-0.1
    if(enemy1X<0):
        enemy1X_C=0.1

    if(enemy2X>736):
        enemy2X_C=-0.1
    if(enemy2X<0):
        enemy2X_C=0.1


    if(bulleton):
        bulletplacer(bulletX,bulletY)
        bulletY+=bulletY_C
        if(bulletY<0):
            bulletX=playerX
            bulletY=playerY
            bulleton=False
    

    hitrange=25   #Make the number smaller to increase difficulty
    
    if(abs(bulletX-enemyX)<hitrange and abs(bulletY-enemyY)<hitrange):
        #print("HIT")       
        
        explosionplacer(enemyX,enemyY)
        time.sleep(0.5)
        score+=1
        print(score)
        enemyY=random.randint(0,200)
        enemyX=random.randint(0,200)
        
    if(abs(bulletX-enemy1X)<hitrange and abs(bulletY-enemy1Y)<hitrange):                        #collision detection
        #print("HIT")
        
        explosionplacer(enemy1X,enemy1Y)
        time.sleep(0.5)
        score+=1
        print(score)
        enemy1Y=random.randint(0,200)
        enemy1X=random.randint(0,200)
    if(abs(bulletX-enemy2X)<hitrange and abs(bulletY-enemy2Y)<hitrange):
        #print("HIT")        
        
        explosionplacer(enemy2X,enemy2Y)
        time.sleep(0.5)
        score+=1
        print(score)
        enemy2Y=random.randint(0,200)
        enemy2X=random.randint(0,200)
    

    green = (0, 255, 0)
    red=(255,0,0)
    font = pygame.font.Font('freesansbold.ttf', 32)
    scoretext=font.render("score"+str(score),True,green,red)     

    screen.blit(scoretext,(650,500))
    #screen.blit(bulletimage,(playerX,playerY))

    enemyplacer(enemyX,enemyY)
    enemy1placer(enemy1X,enemy1Y)
    enemy2placer(enemy2X,enemy2Y)
    #explosionplacer(500,500)
    
    #print(enemyX)
    enemyX+=enemyX_C
    enemy1X+=enemy1X_C
    enemy2X+=enemy2X_C         
    pygame.display.update()

    