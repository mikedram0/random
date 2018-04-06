from vpython import *
import math
ke = 9e9
scene = canvas(width = 1280, height = 720)
positive = sphere(pos = vector(0,0,0), color = color.red, radius = 10)

theta=0
fi=0
r=10
for theta in range(0,360,1):
    for fi in range(0,360,1):
        i=r*sin(math.radians(fi))*cos(math.radians(theta))
        j=r*sin(math.radians(fi))*sin(math.radians(theta))
        k=r*cos(math.radians(fi))
        if(i==0 and j==0 and k==0):
            print("ERROR_EVENT_HANDLED")

        else:
            rpos = vector(i,j,k)
            fieldpos = 9e9/mag(rpos)**2 
            totalfield = fieldpos 
            field1 = arrow(pos = vector(i,j,k), axis = (rpos),length= abs(totalfield)/1000 )

'''
step=100

for i in range(-1000,1000,step):
    for j in range(-1000,1000,step):
        for k in range(-1000,1000,step):
            if(i==0 and j==0 and k==0):
                print("ERROR_EVENT_HANDLED")

            else:
                rpos = vector(i,j,k)
                fieldpos = 9e9/mag(rpos)**2 
                totalfield = fieldpos 
                field1 = arrow(pos = vector(i,j,k), axis = (rpos),length= abs(totalfield)/1000 )
'''
