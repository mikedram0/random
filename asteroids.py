import sys, pygame,time
pygame.init()

size = width, height = 800, 600
black = 0, 0, 0

screen = pygame.display.set_mode(size)

ship = pygame.image.load("starship.png")
shiprect = ship.get_rect()
x=width/2
y=height/2
vx=0.1
vy=0.1

while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()


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

	ship=pygame.transform.rotate(ship,2)
	shiprect = ship.get_rect()
	#time.sleep(100)

	screen.fill(black)
	screen.blit(ship, (x,y))
	pygame.display.update()

pygame.quit()
quit()
