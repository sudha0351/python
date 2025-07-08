"""Logical operators are used to perform logical operations 
they are logical and , or , not 
and -- if both the conditions are true it returns the true 
T T T 
F T F 
T F F 
F F F 
or --- if one of the condition is true it returns the true 
T F T 
F T T 
T T T 
F F F 
not -- it just negotiates the condition 
T F 
F T 
"""
# program                                       
a = 13 
b = 45 
c= a>=34 and b<=50 
print(c) 
d = 67 
e = 89 
f = d!=67 or e==89 
print(f) 
a = 10 
print(not(a))#F 
b = 0 
print(not(b))#T