#終極密碼猜數字
import random
ans=random.randint(0,100)
player=int(input("Enter a number: "))
while True:
	if player>ans:
		print("Too big")
		player=int(input("Enter a number: "))
		continue
	elif player<ans:
		print("Too small")
		player=int(input("Enter a number: "))
		continue
	else:
		print("Correct")
		break
