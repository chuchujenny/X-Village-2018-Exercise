#LEGB practice
#3-1
#Python會依L->E->G->B的順序，從最內層(L)往外層的順位開始尋找變數
#global scope (第5行~第19行) 
x = 23

def f():
    print('x1:', x)    #local scope

y = 23
def g(y, w):
    y = 22             #\
    print('y1:', y)    #-->這三行也是local scope
    print('w1:', w)    #/
    
f()
print('x2:', x)
g(10, 12)
print('y2:', y)

'''
x1: 23 --> f()此函數中沒有x，所以往外一層找到x=23，所以x1=23
x2: 23 --> 第17行本身就在global scope，x=23，所以x2=23
y1: 22 --> 定義g(y,w)函數會輸出y=22，所以不論輸入的y值為多少，最後輸出的y1都會等於y=22
w1: 12 --> w為函數輸入值，因此print("w1",w)時，w就會直接套用輸入的w值
y2: 23 --> 第19行本身就在global scope，y=23，所以y2=23
'''

#3-2
x = 99   #此 x 屬於global scope
m = 11   #此 m 屬於global scope

def f(y, w): 
    z = x + y  # 此z,y 屬於local scope，取的x值是從global scope的x來的
    w = w + 1  # 此w 屬於local scope
    m = 12     # 此m 屬於local scope
    return z

value = f(1, 2) #value 屬於global scope

