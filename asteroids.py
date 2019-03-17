import pygame
pygame.init()
pygame.display.set_caption("Asteroids")

class game:
	def __init__(self,height,widht,count):
		self.height=height
		self.widht=widht
		self.loop=1
		self.count=count
		self.gameDisplay=pygame.display.set_mode((self.widht,self.height))

	def main(self):
		self.loop=1
		while self.loop==1:
			for i in range(self.count):
				print("hey")
			self.loop=0

game1=game(900,1600,50)
game1.main()
