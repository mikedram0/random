import sys
import pygame
import time
import math
pygame.init()

size = width, height = 640, 480
#size = width, height = 1600, 900
black = 0, 0, 0

#screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen = pygame.display.set_mode((width, height))

ship = pygame.image.load("starship.png")
bullet_img = pygame.image.load("bullet.png")
shiprect = ship.get_rect()
x=width/2
y=height/2
vx=0
vy=0
angle=0
anglev=0
FPS=60
bullets=[]

class Bullet:
    def __init__(self,bposx,bposy):
        self.bposx=bposx
        self.bposy=bposy
        self.bvx=math.sin(angle*3.1415/180 +3.1415) 
        self.bvy=math.cos(angle*3.1415/180+3.1415)
       # self.fire()

    def checkdelete(self):
        if self.bposx >width or self.bposx<0 or self.bposy > height or self.bposy < 0:
        	bullets.remove(self)

    def draw(self):
        screen.blit(bullet_img, (self.bposx,self.bposy))
        
    def move(self):
        self.bposx=self.bposx+self.bvx*20
        self.bposy=self.bposy+self.bvy*20

while 1:
    time.sleep(1/FPS)
    angle=angle+anglev
    #print(1)
    for event in pygame.event.get():
        #print(2)
        if event.type == pygame.QUIT: 
            sys.exit()
        if event.type == pygame.KEYDOWN:
            
            if event.key==pygame.K_ESCAPE:
                sys.exit()

            if event.key==pygame.K_a:
                anglev=anglev+1

            if event.key==pygame.K_SPACE:
                bullets.append(Bullet(x,y))
                print("piew")
                

            if event.key==pygame.K_d:
                anglev=anglev-1


            if event.key == pygame.K_w:
                vx += math.sin(angle*3.1415/180 +3.1415) 
                vy += math.cos(angle*3.1415/180+3.1415) 


    x += vx
    y += vy

    if x-shiprect[2]>width:
        x = 0 - shiprect[1]
    if x+shiprect[2]<0:
        x = width
    if y>height:
        y = 0 - shiprect[3]
    if y<0-shiprect[3]:
        y = height
        
    print(bullets)
    old=shiprect.center
    new_ship=pygame.transform.rotate(ship,angle)
    shiprect = new_ship.get_rect()
    shiprect.center=old




    screen.fill(black)

    for bullet in bullets:
        bullet.checkdelete()
        if bullets.count(bullet):
            bullet.move()
            bullet.draw()


    screen.blit(new_ship, (x,y))
    pygame.display.update()

pygame.quit()
quit()
