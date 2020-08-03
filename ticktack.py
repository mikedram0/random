grid = [' ',' ',' ',' ',' ',' ',' ',' ',' ']

width = 3
height = 3

def getvalue(x,y):
	return grid[x + width*y]

def setvalue(x,y,value):
	grid[x + width*y] = value

def displaygrid():
	x = 0
	for i in grid:
		if x == 3:
			print('\n' , sep='', end='')
			x = 0
		print(i ,end='',sep=' ' )
		x += 1

def checkgrid():
	for x in range(3):
		for y in range(3):
			try:
				if (getvalue(x,y) == getvalue(x+1,y) == getvalue(x+2,y) != ' ') or (getvalue(x,y) == getvalue(x,y+1) == getvalue(x,y+2) != ' ') or (getvalue(x,y) == getvalue(x+1,y+1) == getvalue(x+2,y+2) != ' ') or (getvalue(x,y) == getvalue(x-1,y+1) == getvalue(x-2,y+2) != ' ' ):
					print("\nEND\n")
			except:
				pass


while(True):

	displaygrid()
	coords1 = str(input("\nPlayer 1: "))
	coords1 = coords1.split(",")
	if len(coords1) == 2 and getvalue(int(coords1[0]),int(coords1[1])) == ' ':
		setvalue(int(coords1[0]),int(coords1[1]),'x')
	else: continue

	checkgrid()

	displaygrid()
	coords2 = str(input("\nPlayer 2: "))
	coords2 = coords2.split(",")
	if len(coords2) == 2 and getvalue(int(coords2[0]),int(coords2[1])) == ' ':
		setvalue(int(coords2[0]),int(coords2[1]),'o')
	else: continue

	checkgrid()
