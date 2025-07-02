"Bitwise operators are used to perform the binary operations"
"""
bitwise and -- & if both the bits are 1 it returns the 1
bitwise or -- | if one of the bit is 1 its returns the 1 else 0
bitwise XoR-- ^ if one of the bit is 1 its returns 1 if both the bits are 1 its returns 0
"""
a = 3 #0011
b = 4#0100
c = a&b#0000
print(c)

d = a|b # 0111--7
print(d)

e = 8#1000
f = 11#1011
g = e^f#0011--3
print(g)
