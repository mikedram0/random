import sys, pygame
pygame.init()

size = width, height = 320, 240
black = 0, 0, 0

screen = pygame.display.set_mode(size)

ship = pygame.image.load("starship.png")
x=width/2
y=height/2
vx=0.02
vy=0.03

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    x += vx
    y += vy

    #if x>width:

    screen.fill(black)
    screen.blit(ship, (x,y))
    pygame.display.flip()
