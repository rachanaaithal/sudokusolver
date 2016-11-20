'''
def que(x):
	m=[]
	print('enter the numbers line by line:')
	for i in range(9):
		a=input('>')
		m.append(a)
	x[0]=process(m)
	#return x


def process(m):
	n=[]
	for i in m:
		x=[]
		for j in i:
			x.append(int(j))
		n.append(x)
	return(n)
'''

def que(x):
	f=open('sud.txt','r')
	for i in range(9):
		m=f.readline()

		x[0][i]=process(m)

	f.close()

def process(m):
	n=[]
	l=m.split(',')
	for i in l:
		n.append(int(i))
	return(n)




def output(x):
	for i in range(9):
		for j in range(9):
			print (x[0][i][j],end='\t')
		print()



def fill(x,i,j):
	#fill horizontal and vertical
	for a in range(9):
		x[x[0][i][j]][i][a]=0
		x[x[0][i][j]][a][j]=0
		x[a+1][i][j]=0

	#fill square
	a=j//3
	b=i//3
	for u in range(9):
		for v in range(9):
			if v//3==a and u//3==b:
				x[x[0][i][j]][u][v]=0





def makex(x):
	for i in range(9):
		for j in range(9):
			if x[0][i][j]!=0:
				fill(x,i,j)




def num(x,i,j):
	res=0
	l=[]
	for k in range(1,10):
		if x[k][i][j] !=0:
			l.append(k)
	if len(l)==1:
		res=l[0]
	return(res)





def solve(x,y):
	if x!=y:
		y=copy.deepcopy(x)
		for i in range(9):
			for j in range(9):
				if x[0][i][j]==0:
					z=num(x,i,j)
					if z !=0:
						x[0][i][j]=z
						fill(x,i,j)
		return solve(x,y)
	else:
		return x


import copy
def main():
	x=[[[k for i in range(9)]for j in range(9)]for k in range(10)]
	y=copy.deepcopy(x)
	que(x)
	makex(x)
	fin=solve(x,y)
	output(fin)



main()