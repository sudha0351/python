"""
A if within a if is called nested if 
NOTE: In order to execute inner else outer if condition must be true
syntax :
if condition :
    outer if statements 
    if condition :
        inner if statements
    else:
        inner else statements 
else:
    outer else statements
    """

#program for nestedif
a = 10
b = 20
c = 30
if a==10 and c==30:
    print("the outer if executed")
    if a==10:
        print("the inner if executed")
    else :
        print("the inner else executed") 
else:
    print("the outer else executed")