# we have 4 types to represent data in int
"""
decimal binary octal and hexa
"""
# by default python is int decimal form
a=1111

print(a) #decimal

a=0b1111
print(a) #binary

# we can also represent the -ive the same way

a=-0B1111
print(a)

a=-1111
print(a)

# OCTAL b-8 mean 0 to 7
a=777 # mean decimal
print(a)
a=0o777
print(a)

#HEXA
a=0xFaCe
print(a)

# remember output will always be in decimal form

a=10
b=0b10
c=0O10
d=0x10
print("D  B O  H")
print(a,b,c,d)