import pygame

pygame.init()

height=900
widht=1600

gameDisplay=pygame.display.set_mode((widht,height))
pygame.display.set_caption("Asteroids")

play=True

while play==True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT():
			play=False
		pygame.display.update()
		clock.tick(60)

pygame.quit()
quit()
