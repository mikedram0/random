import sys
import pygame
import time
pygame.init()

size = width, height = 800, 600
black = 0, 0, 0

screen = pygame.display.set_mode(size)

ship = pygame.image.load("starship.png")
shiprect = ship.get_rect()
x=width/2
y=height/2
vx=0
vy=0
ancle=0
anclev=0
FPS=60

while 1:
	time.sleep(1/FPS)
	ancle=ancle+anclev
	#print(1)
	for event in pygame.event.get():
		#print(2)
		if event.type == pygame.QUIT: 
			sys.exit()
		if event.type == pygame.KEYDOWN:
			print(3)

			if event.key==pygame.K_a:
				anclev=anclev+1
				print(4)

			if event.key==pygame.K_d:
				anclev=anclev-1

			if event.key==pygame.K_w:
				pass




	x += vx
	y += vy

	if x>width-shiprect[2]:
		x = width - shiprect[2]
		vx *= -1
	if x<0:
		x = 0
		vx *= -1
	if y>height-shiprect[3]:
		y = height - shiprect[3]
		vy *= -1
	if y<0:
		y = 0
		vy *= -1

	old=shiprect.center
	new_ship=pygame.transform.rotate(ship,ancle)
	shiprect = new_ship.get_rect()
	shiprect.center=old

	screen.fill(black)
	screen.blit(new_ship, (x,y))
	pygame.display.update()

pygame.quit()
quit()
