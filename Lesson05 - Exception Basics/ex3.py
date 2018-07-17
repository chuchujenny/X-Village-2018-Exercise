def function(a,b):
    if type(a) != int:
        raise ValueError("invalid literal for int() with base 10: ",a )
    if type(b) != int:
        raise NameError("invalid literal for int() with base 10: " ,b )
    else: return a*a*b

num1=function(8,"y")
print(num1)