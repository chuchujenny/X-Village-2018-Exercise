#class life (no __init__)
class Map:
	def set_map(self,n):
		k= int((n-1)*(1/2))    #設正中央那行在list內的index 為 k，用n代換成k ex. if n=5，則index為0,1,2,3,4，所以k=2
		i=1
		j=1
		m=[]
		self.matrix=[]
		while i <= n:         #利用while迴圈建構list中有list的結構，i為最外面list的長度，j為list中的list的長度 
			while j<= n:      #ex. k=3會印出[['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]
				m+=["*"]      				
				j+=1
			self.matrix+=[m]
			j=1
			m=[]
			i+=1 
	def set_pattern(self,p):
		n=len(self.matrix)
		k= int((n-1)*(1/2))
		if p == 1:                             #當符合條件時，將指定位置代換成0
			self.matrix[k-1][k-1:k+2]=[0,0,0] 
			self.matrix[k][k-1]=0
			self.matrix[k+1][k]=0
		else:
			pass

	def display(self):                        #用while迴圈讓他一個一個印出來 每印完一列就換行
		i=0
		j=0
		while i <len(self.matrix):
			while j< len(self.matrix):
				print(self.matrix[i][j],end="")
				j+=1
			print("")
			j=0
			i+=1

my_map=Map()
my_map.set_map(5)
my_map.display()
print(" ")                     #這樣print出的東西空了一行，才不會黏在一起
my_map.set_pattern(1) 
my_map.display()