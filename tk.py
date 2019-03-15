import tkinter as tk

app = tk.Tk()

canv = tk.Canvas(app , bg ="blue" ,height = 250, width = 300)
radius = 50
x=150
y=125
c1 = canv.create_oval(x-radius,y-radius,x+radius,y+radius)


canv.pack()
app.mainloop()
