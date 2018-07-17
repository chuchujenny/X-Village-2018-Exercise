#ex4 自己定義一個 exception 叫作 RelationException

class RelationException(Exception):
    def __init__(self, pa, pb):
        self.msgA = pa
        self.msgB = pb
    def __str__(self):
        return "No relation found"+ "\n" +"Are you sure that " + self.msgA + " and " + self.msgB + " are in love with each other?" 

relation = {'Jason':'Mary', 'Mary':'Jason', 'Jennifer':'Ken', 'Ken':'Jennifer', 'Tina':'Kim', 'Kim':'Tina'}
def check(pa, pb):
    if relation[pa] != pb:
    	raise RelationException(pa,pb)


try:
    p1 = input("Please enter the first person: ")
    p2 = input("Please enter the second person: ")
    check(p1, p2)
    print("{} and {} are in love with each other!".format(p1, p2))

except RelationException as e:
    print(e)