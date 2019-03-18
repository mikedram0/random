import sys
import pygame
import time
import math
import random

pygame.init()

size = width, height = 1920, 1080
#size = width, height = 1600, 900
black = 0, 0, 0

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
#screen = pygame.display.set_mode((width, height))

ship = pygame.image.load("starship.png")
bullet_img = pygame.image.load("bullet.png")
asteroid_img = pygame.image.load("asteroid_img.png")
shiprect = ship.get_rect()
x=width/2
y=height/2
vx=0
vy=0
angle=0
anglev=0
FPS=60
bullets=[]
asteroids_list=[]

class asteroid:
	def __init__(self):
		self.aposx=random.randint(0,width)
		self.aposy=random.randint(0,height)
		self.avx=random.randint(-5,5)
		self.avy=random.randint(-5,5)

	def draw(self):
		self.aposx=self.aposx+self.avx
		self.aposx=self.aposx+self.avy
		screen.blit(asteroid_img, (self.aposx,self.aposy))


class Bullet:
	def __init__(self,bposx,bposy):
		self.bposx=bposx
		self.bposy=bposy
		self.bvx=math.sin(angle*3.1415/180 +3.1415) 
		self.bvy=math.cos(angle*3.1415/180+3.1415)
        # self.fire()

	def fire(self):
        
		print("test")

	def draw(self):
		self.bposx=self.bposx+self.bvx*20
		self.bposy=self.bposy+self.bvy*20
		screen.blit(bullet_img, (self.bposx,self.bposy))

while 1:
	time.sleep(1/FPS)
	angle=angle+anglev
	asteroids_list.append(asteroid())
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
        

	old=shiprect.center
	new_ship=pygame.transform.rotate(ship,angle)
	shiprect = new_ship.get_rect()
	shiprect.center=old




	screen.fill(black)

	for aster in asteroids_list:
		aster.draw()

	for bullet in bullets:
		bullet.draw()


	screen.blit(new_ship, (x,y))
	pygame.display.update()

pygame.quit()
quit()
