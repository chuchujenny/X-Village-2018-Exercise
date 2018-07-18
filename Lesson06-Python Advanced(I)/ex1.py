#a=[[0, 0], [1, 4], [2, 7], [3, 5], [4, 2], [5, 6], [6, 1], [7, 3]]
#a=[1,1,1,2,2,3,3,3,4,4,4,5,5]

def eight_queens(a):
	p=[]
	q=[]
	r=[]
	s=[]
	for i in range(0,len(a)):
		p+=[a[i][0]]
		q+=[a[i][1]]
		r+=[sum(a[i])]
		s+=[a[i][1]-a[i][0]]
	item_p=set(p)
	item_q=set(q)
	item_r=set(r)
	item_s=set(s)
	m=0
	n=0
	l=0
	k=0
	
	for i in item_p:
		m+=p.count(i)
	if m==8:
		print("True")
	for i in item_q:
		n+=q.count(i)
	if n==8:
		print("True")
	for i in item_r:
		l+=r.count(i)
	if l==8:
		print("True")
	for i in item_s:
		k+=s.count(i)
	if k==8:
		print("True")
	



y=eight_queens([[0, 0], [1, 4], [2, 7], [3, 5], [4, 2], [5, 6], [6, 1], [7, 3]])








#for i in range(0,len(a)):
#	if a[i][1] != 

'''
def eight_queens(a):
k=[]
for i in range(0,8):
	a[i][0]
'''