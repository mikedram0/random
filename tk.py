import tkinter as tk
import random

top = tk.Tk()
canv=tk.Canvas(top, bg="white", height=250, width=300)
list=[]

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
    circle = coll_obj(random.randint(25,50),random.randint(0,300),random.randint(0,250),5,2)
    circle.draw()
    list.append(circle)








list[0].move()
list[0].draw()
canv.pack()



top.mainloop()



