from vpython import *


ke = 9e9


scene = canvas(width = 1280, height = 720)


positive = sphere(pos = vector(0,0,0), color = color.red, radius = 10)
#neg = sphere(pos = vector(100,0,0), color = color.blue,radius = 10)

'''
for i in range(-1000,1000,100):
    for j in range(-1000,1000,100):
        rpos = vector(i,j,0)-pos.pos
        rneg = vector(i,j,0)-neg.pos
        fieldpos = (-ke/(mag(rpos)**2)) * (rpos/mag(rpos))
        fieldneg = (ke/(mag(rneg)**2)) * (rneg/mag(rneg))
        totalfield = fieldpos + fieldneg
        field = arrow(pos = vector(i,j,0), axis = (totalfield/mag(totalfield)),length= mag(totalfield)/5000 )
'''
for i in range(-1000,1000,50):
    for j in range(-1000,1000,50):
        rpos = vector(i,j,0)
        fieldpos = (float(9e9)/float((mag(rpos)**2))) 
        totalfield = fieldpos 
        field1 = arrow(pos = vector(i,j,0), axis = (rpos),length= abs(totalfield)/10000 )
        field2 = arrow(pos = vector(-i,j,0), axis = vector(-rpos.x,rpos.y,rpos.z),length= abs(totalfield)/10000 )

