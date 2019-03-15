import tkinter as tk
import random

canvh=600
canvw=800
top = tk.Tk()
canv=tk.Canvas(top, bg="white", height=canvh, width=canvw)
list1=[]

class coll_obj:
    def __init__(self,radius,x,y,vx,vy):
        self.radius=radius
        self.x=x
        self.y=y
        self.vx=vx
        self.vy=vy
	
    def draw(self):
        c = canv.create_oval(self.x-self.radius,self.y-self.radius,self.x+self.radius,self.y+self.radius)
    def move(self):
        self.x += self.vx
        self.y += self.vy


for circle in range(1):
    circle = coll_obj(random.randint(25,50),random.randint(0,canvw),random.randint(0,canvh),5,2)
    circle.draw()
    list1.append(circle)


i=0
while(i<1000):
	canv.delete("all")
	list1[0].draw()
	list1[0].move()
	print("test")
	canv.pack()
	top.update()
	i=i+1
	#top.mainloop()
