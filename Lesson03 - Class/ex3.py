#class life (with __init__)
class Map:
	def __init__(self,k,p):
		n= int((k-1)*(1/2))    #設正中央那行在list內的index 為 n，用k代換成n ex. if k=5，則index為0,1,2,3,4，所以n=2
		i=1
		j=1
		m=[]
		self.matrix=[]
		while i <= k:         #利用while迴圈建構list中有list的結構，i為最外面list的長度，j為list中的list的長度 
			while j<= k:      #ex. k=3會印出[['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]
				m+=["*"]      				
				j+=1
			self.matrix+=[m]
			j=1
			m=[]
			i+=1 
		if p == 1:                             #當符合條件時，將指定位置代換成0
			self.matrix[n-1][n-1:n+2]=[0,0,0] 
			self.matrix[n][n-1]=0
			self.matrix[n+1][n]=0
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

glider_map=Map(7,1)
glider_map.display()
