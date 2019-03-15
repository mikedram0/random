import tkinter as tk
import random
import time
import math
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
            if math.sqrt((circle.x-self.x)**2+(circle.y-self.y)**2)<= self.radius + circle.radius:
                temp = self.x
                self.x = circle.x
                circle.x = temp
                temp = self.y
                self.y = circle.y
                circle.y = temp
            


for circle in range(10):
    circle = coll_obj(random.randint(25,50),random.randint(0,300),random.randint(0,250),random.randint(-20,20),random.randint(-20,20))
    circle.draw()
    list1.append(circle)



while(1):
    canv.delete("all")
    for circle in list1:
        circle.move()
        circle.collision()
        circle.draw()
    time.sleep(0.005)
    canv.pack()
    top.update()
    #top.mainloop()
