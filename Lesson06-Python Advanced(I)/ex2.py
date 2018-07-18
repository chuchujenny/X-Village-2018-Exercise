#凱薩加密提示
#print(chr(122)) #z
#print(chr(97))  #a
#print(ord("x"))

def caesar_cipher(word,n):
	for i in range(0,len(word)):
		if (ord(word[i])+n) >122:                 #如果大於122就超過z了
			print(chr(ord(word[i])+n-26),end="")  #利用-26讓他回到字母開頭從頭繼續接著數
		else:
			print(chr(ord(word[i])+n),end="")

y=caesar_cipher("xvillage",6)

