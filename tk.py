import tkinter as tk
import random
import time
import math
import threading as thr

class coll_obj:
	def __init__(self,radius,x,y,vx,vy):
		self.radius=radius
		self.x=x
		self.y=y
		self.vx=vx
		self.vy=vy
		self.mass = self.radius**2
		self.draw()
	
	def draw(self):
		self.id = game1.canv.create_oval(self.x-self.radius,self.y-self.radius,self.x+self.radius,self.y+self.radius,fill="white",tags="ball")
	def move(self):
		self.x += self.vx
		self.y += self.vy
		#canv.move(self.id,self.vx,self.vy)
	def bordercollision(self):
		if self.x  > canvw - self.radius:
			self.x = canvw - self.radius 
			self.vx *= -1
		if self.x < self.radius:
			self.x = self.radius
			self.vx *= -1
		if self.y > canvh - self.radius:
			self.y = canvh - self.radius
			self.vy *= -1
		if self.y < self.radius:
			self.y = self.radius
			self.vy *= -1
	def btbcollision(self):
		for circle in list1:
			if circle == self:
				continue
			dist = math.sqrt((circle.x-self.x)**2+(circle.y-self.y)**2)
			if dist <= self.radius + circle.radius:
				try:
					overlap = self.radius + circle.radius - dist

					#Calculating the normal vector and normalizing it

					nx = (circle.x - self.x)/dist
					ny = (circle.y - self.y)/dist
					#Calculating the tangential vector 

		
					tx = ny
					ty = -1*nx

					#Displacing the balls along the parallel axis in case of overlap

					self.x -= nx * overlap/2
					self.y -= ny * overlap/2

					circle.x += nx* overlap/2
					circle.y += ny*overlap/2

					# Here I will use the collison "coordinates" , by breaking the velocity into a tangential and parralell part


					#Calculating the tangential component of velocity , which are not affected by the collision

					vtan1 = self.vx*tx +self.vy*ty
					vtan2 = circle.vx*tx + circle.vy*ty

					#Calculating the parralell velocity before the colision

					vpar1b = self.vx * nx + self.vy * ny
					vpar2b = circle.vx * nx + circle.vy * ny


					#Calculating the parallell velocities after the collision , using the elastic collision formula

					vpar1a = ((self.mass - circle.mass)*vpar1b + 2*circle.mass*vpar2b)/(self.mass + circle.mass)
					vpar2a = (2*self.mass*vpar1b + (circle.mass - self.mass)*vpar2b)/(self.mass + circle.mass)


					#Setting the velocities

					self.vx = vtan1*tx + nx * vpar1a
					self.vy = vtan1*ty + ny * vpar1a

					circle.vx = vtan2*tx + nx * vpar2a
					circle.vy = vtan2*ty + ny * vpar2a
				except:
					pass


class game():
	def __init__(self):
		self.canvh=900
		self.canvw=1600
		self.starting_balls=20
		self.fps=60
		self.list1=[]
		self.main_frame=tk.Tk()
		self.canv=tk.Canvas(self.main_frame, bg="black", height=self.canvh, width=self.canvw)
		self.canv.pack()

	def main(self):
		self.canv.delete("ball")
		self.main_frame.bind("<Button-3>", self.create_balls)
		self.main_frame.bind("<B1-Motion>", self.btn_move)
		#self.main_frame.bind("<ButtonRelease1>", brelease)
		for circle in self.list1:
			circle.move()
			circle.bordercollision()
			circle.btbcollision()
			circle.draw()
		time.sleep(1/self.fps)
		self.main_frame.update()

	def create_balls(self):
		for circle in range(self.starting_balls):
			circle = coll_obj(random.randint(10,20),random.randint(0,canvw),random.randint(0,canvh),random.randint(-5,5),random.randint(-5,5))
			list1.append(circle)

	def btn_move(self):
		try:
			if self.canv.coords("current")!=[]:
				print(self.canv.coords("current"))
			self.tmpl=self.canv.coords("current")
			self.canv.create_line((self.tmpl[2]+self.tmpl[0])/2,(self.tmpl[1]+self.tmpl[3])/2,self.event.x,self.event.y,fill="cyan",width = 2)
		except:
			pass

	def btn_create(self):
		circle = coll_obj(random.randint(10,20),event.x,event.y,0,0)
		circle.draw()
		self.list1.append(circle)
	

game1=game()
for i in range(10000):
	game1.main()
