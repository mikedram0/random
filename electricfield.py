from vpython import *
import math
ke = 9e9
scene = canvas(width = 1600, height = 900)
positive = sphere(pos = vector(-50,0,0), color = color.red, radius = 10)
negative = sphere(pos = vector(50,0,0), color = color.blue, radius = 10)

theta=0
fi=0
r=100
for r in range(100,1000,50):
    for theta in range(0,360,18):
        for fi in range(0,360,18):
            i=r*sin(math.radians(fi))*cos(math.radians(theta))
            j=r*sin(math.radians(fi))*sin(math.radians(theta))
            k=r*cos(math.radians(fi))
            if(i==0 and j==0 and k==0):
                print("ERROR_EVENT_HANDLED")

            else:
                pos = vector(i,j,k)
                vec1 = pos - positive.pos
                vec2 = pos - negative.pos
                fieldpos = 9e9/mag(vec1)**2 * (vec1/mag(vec1))
                fieldneg = -9e9/mag(vec2)**2 * (vec2/mag(vec2))
                totalfield = fieldpos + fieldneg
                field1 = arrow(pos = vector(i,j,k), axis = (totalfield),length= mag(totalfield)/20000 ,shaftwidth = 3)


