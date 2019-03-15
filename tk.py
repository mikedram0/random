import tkinter as tk
import random
import time
import math
import threading as thr
canvh=720
canvw=1280
top = tk.Tk()
canv=tk.Canvas(top, bg="black", height=canvh, width=canvw)
list1=[]


colors = ["white","blue","red","yellow","orange"]

class coll_obj:
	def __init__(self,radius,x,y,vx,vy):
		self.radius=radius
		self.x=x
		self.y=y
		self.vx=vx
		self.vy=vy
	
	def draw(self):
		self.id = canv.create_oval(self.x-self.radius,self.y-self.radius,self.x+self.radius,self.y+self.radius,fill="white")
	def move(self):
		self.x += self.vx
		self.y += self.vy
	def collision(self):
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
		for circle in list1:
			if circle == self:
				continue
			vec = math.sqrt((circle.x-self.x)**2+(circle.y-self.y)**2)
			if vec <= self.radius + circle.radius:
				u1 = math.sqrt((circle.vx)**2 + (circle.vy)**2)
				u2 = math.sqrt((self.vx)**2 + (self.vy)**2)
				phi = math.acos((circle.x-self.x)/vec)
				theta1 = math.acos(circle.vx/u1)
				theta2 = math.acos(self.vx/u2)

				circle.vx = ((2*u2*math.cos(theta2-phi))/2)*math.cos(phi) + u1*math.sin(theta1-phi)*math.sin(phi)
				circle.vy = ((2*u2*math.cos(theta2-phi))/2)*math.sin(phi) + u1*math.sin(theta1-phi)*math.cos(phi)

				self.vx = ((2*u1*math.cos(theta1-phi))/2)*math.cos(phi) + u2*math.sin(theta2-phi)*math.sin(phi)
				self.vy = ((2*u1*math.cos(theta1-phi))/2)*math.sin(phi) + u2*math.sin(theta2-phi)*math.cos(phi)
			


for circle in range(2):
    circle = coll_obj(random.randint(25,50),random.randint(0,300),random.randint(0,250),random.randint(-20,20),random.randint(-20,20))
    circle.draw()
    list1.append(circle)


def main():
    canv.delete("all")
    for circle in list1:
        circle.move()
        circle.collision()
        circle.draw()
    time.sleep(0.005)
    canv.pack()
    top.update()


#for j in range(10000):
#	main()
if __name__ == '__main__':
    for j in range(1000):
        t1 = thr.Thread(target=main())
        t1.start()
