
import tkinter as tk
import random

top = tk.Tk()
canv=tk.Canvas(top, bg="white", height=250, width=300)
list1=[]
#last_num=0

class coll_obj:
	def __init__(self,radius,x,y):
		self.radius=radius
		self.x=x
		self.y=y
	def create(self):
		c = canv.create_oval(self.x-self.radius,self.y-self.radius,self.x+self.radius,self.y+self.radius)


#c1 = coll_obj(50,150,125)

for circle in range(10):
    circle = coll_obj(random.randint(25,50),random.randint(0,300),random.randint(0,250))
    circle.create()
    list1.append(circle)
	    

#def new_obj():
#	global list1,last_num
#	list1.append("c"+str(last_num+1))
#	print(list1)
#	#str(list1[last_num+1])=coll_obj(random.randint(25,50),random.randint(0,300),random.randint(0,250))
#	last_num=last_num+1              

canv.pack()
#for i in range(10):
#	new_obj()
top.mainloop()
