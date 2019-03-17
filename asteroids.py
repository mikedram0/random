import sys, pygame,time,math
pygame.init()

size = width, height = 800, 600
black = 0, 0, 0

screen = pygame.display.set_mode(size)

ship = pygame.image.load("starship.png")
shiprect = ship.get_rect()
x=width/2
y=height/2
vx=0.0
vy=0.0

angle=60




while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                vx += math.sin(angle*3.1415/180 +3.1415) *0.1
                vy += math.cos(angle*3.1415/180+3.1415) *0.1


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



    #angle += 0.1
    old=shiprect.center
    new_ship=pygame.transform.rotate(ship,angle)
    shiprect = new_ship.get_rect()
    shiprect.center=old
    
    screen.fill(black)
    screen.blit(new_ship, (x,y))
    pygame.display.update()

pygame.quit()
quit()
