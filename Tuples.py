"""
Tuples is a collection of items/values/elements
they are enclose within the parenthesis or 
open brackets()seperated by(,)
AS Tuples are immutable it mean we can go with tuples
so when the data is fixed we can go  with tuples..
"""

#eg1:
mytuple=(13,12,11)
print(type(mytuple))#<class tuple>
mytuple2=()#empty tuple
print(type(mytuple2))#<class tuple>
mytuple3=(10)
print(type(mytuple3))#<class int>

"""
Note:when you wanna created a tuple with single value 
it should be seperated by so that the complier 
treats as tuple or else it just treats as integer
"""
#creation of tuple 
#syntax:tuple variable =(val1,val2,val3..valn)
mytuple5=(12,23,45,34,67,56+78j,[12,34,45] ,"hello",(123,"ece"))
print(mytuple5)
#creating a tuple with a list 
t=[23,45,56,"jj"]
print(t)
k=tuple(t)
print(k)
#creating the tuple with "tuple" predefined word
t=tuple()#it consider as empty tuple 
print(t)