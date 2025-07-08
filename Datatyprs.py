"""
Datatypes tells about the type of data that a variable is holding on
1.Number
2. Sequence
3. Boolean
4. Set
5. Dictionary
"""
#Number
"""
Interger -- which can represented as int() which holds all the positive and negative whole numbers
o to n and o to -n
Float ---- which can respresented as float()which holds all the fractional or decimal values
o to n.n and o to -n.n
Complex --- which can be represented as complex()which holds some real and imaginary values
which represents as ai+bj ai-- real bj--imaginary(future predicted value)
"""
a = 78
print(a)
#type--which tells about the datatype
print(type(a)) #<class 'int'>
#Where all the python datatypes are there it was in a class
#id ---which tells about the address location of a variable value
print(id(a))#longest integer

a1= -45
print(a1)
print(type(a1))
print(id(a1))

#float
b = 567.789
print(b)
print(type(b))
print(id(b))

b1= -89.90
print(b1)
print(type(b1))
print(id(b1))

c = 34+78j
print(c)
print(type(c))
print(id(c))

c1= -345+34j
print(c1)
print(type(c1))
print(id(c1))

"""
sequence datatypes - string/ List/ Tuple
"""
#string -- its a collection of characters
# a string can be enclosed either in single quotes('') or double quotes


a = "ists"
print(a)
print(type(a)) #<class 'string'>
print(id(a))

v = 'ece'
print(v)
print(type(v))
print(id(v))
"""
list is a collection of items/values/elements 
it can be represnted by [] and values are seperated by comma
syntax: listname = [val1,val2,..valn]
list is mutable -- we can change them 
"""
mylist = [11, 23.45, 45+6j,[1,2,3],"ece"]#values/items/elements--5
print(mylist)
print(type(mylist))
#acessing the elements
#list elemenets can be accessed using the index
print(mylist[2])#45+6j
print(mylist[4])#ece
#Mutating or changing the elements in a list
mylist[1]= "python"
print(mylist)
mylist[4] ="john"
print(mylist)

"""
Tuple -- Its a collection of items/values/elements
it can be represented by ()and seperated by values(CSV)
tuple is immutable -- unchangable
syntax: tuplename = (val1,val2..valn)
"""
mytupple=(12, 23.45, 45+78j, "ece", [1,23,34],(23,34,45))#elements/items/values--6
print(mytupple)
print(type(mytupple))
#Acessing the elements in the tuple
#using the indexing we can acess the elements
print(mytupple[5])#(23,34,45)
print(mytupple[3])#ece


"""
Boolean Datatypes: It just checks the condition and gives True or False
"""
a = True
print(type(a))

b = False
print(type(b))

"set is a collection of items it can be enclosed in flower braces"
#syntax: setname = {val1,val2,...valn}
myset = {12,23.34, 45+67j, "ece", (12,23,45), True}
print(myset)
print(type(myset))

"dictionary is a collection of key value Pairs enclosed in flower braces"
#syntax : dictname = {key1:val1, key2:val2, key3:val3..keyn:valn}
#Elements in dictionary can be accessed using the keys
#key is a unique one

mydict = {"name":"john", "age":28,"height":6.0, "weight":80}
print(mydict)
print(type(mydict))
print(mydict["name"])#John
print(mydict["weight"])#80