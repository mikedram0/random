import tkinter as tk
import random
import time
import math
import threading as thr
#canvh=900
#canvw=1600

#top = tk.Tk()
#canv=tk.Canvas(top, bg="black", height=canvh, width=canvw)
#canv.pack()
#fps = 60
#list1=[]




class Ball:
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
	def __init__(self,root):
		self.canvh=480
		self.canvw=640
		self.starting_balls=10
		self.fps=60
		self.ball_list=[]
		self.root=root
		self.canv=tk.Canvas(self.root, bg="black", height=self.canvh, width=self.canvw)
		self.canv.pack()
		self.create_balls()

	def main(self):
		self.canv.delete("ball")
		#self.root.bind("<Button-3>", btn_input)
		#self.root.bind("<B1-Motion>", btn_mot)
		#top.bind("<ButtonRelease1>", brelease)
		for circle in self.ball_list:
			circle.move()
			circle.bordercollision()
			circle.btbcollision()
			circle.draw()
		time.sleep(1/self.fps)
		self.root.update()



	def create_balls(self):
		for circle in range(self.starting_balls):
			self.ball_list.append(Ball(random.randint(10,20),random.randint(0,self.canvw),random.randint(0,self.canvh),random.randint(-5,5),random.randint(-5,5)))

	def btn_move(self):
		pass

	def btn_create(self):
		circle = coll_obj(random.randint(10,20),event.x,event.y,0,0)
		circle.draw()
		self.ball_list.append(circle)








	def btn_mot(event):
		global list1
		tmpl=[0,0,0,0]
		try:
			if canv.coords("current")!=[]:
				print(canv.coords("current"))
			tmpl=canv.coords("current")
			canv.create_line((tmpl[2]+tmpl[0])/2,(tmpl[1]+tmpl[3])/2,event.x,event.y,fill="cyan",width = 2)
		except:
			pass


root = tk.Tk()
game1=game(root)
for i in range(10000):
	game1.main()







#while 1:
#	main()
#if __name__ == '__main__':
#    for j in range(10000):
#        t1 = thr.Thread(target=main())
#        t1.start()
