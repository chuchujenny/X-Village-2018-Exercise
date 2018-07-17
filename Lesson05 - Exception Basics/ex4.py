#ex4 自己定義一個 exception 叫作 RelationException
class RelationException(Exception):
    def __init__(self, peopleA, peopleB):
        self.msgA = peopleA
        self.msgB = peopleB
    def __str__(self):
        return "Are you sure that " + self.msgA + " and " + self.msgB + " are in love with each other?" 

try:
    raise RelationException("Mommy", "Daddy")
except RelationException as e:
    print(e)