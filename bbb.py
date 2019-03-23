#import os

list1=[]
n = 99999999999999999999999999999999999
for i in range(n):
	print(i*100/n,"%")
	#os.system('cls')

	isGood = True
	for j in str(i):
		if j=='0':
			isGood = False
			break
	if isGood:
		list1.append(i)
f=open("C:\\Users\\mike\\Desktop\\a.txt","w")

for i in list1:
	f.write(str(i)+"\n")


print("kai omos teliosa maki")
f.close()
