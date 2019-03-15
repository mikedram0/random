import tkinter as tk

top = tk.Tk()
canv=tk.Canvas(top, bg="black", height=250, width=300)

class coll_obj:
	def __init__(self,radius,x,y):
		self.radius=radius
		self.x=x
		self.y=y

	def create(self):
		c = canv.create_oval(self.x-self.radius,self.y-self.radius,self.x+self.radius,self.y+self.radius)


canv.pack()
top.mainloop()
