

print(2+2)
print(10/4)
print(10%3)
print(10//3)
print(10**3)
print(1+2*3**2**2//2/2-3)

a = 132
b = 45
fmt0 = '{:<10}'
fmt1 = '0b{:08b}0x{:02x}'
n = 30

#AND
print("bitwise AND:")
print(fmt0.format('a'), fmt1.format(a,a,a))
print(fmt0.format('b'), fmt1.format(b,b,b))
print('-'*n)
print(fmt0.format('a&b'),fmt1.format(a&b,a&b,a&b))

#OR
print("bitwise OR:")
print(fmt0.format('a'), fmt1.format(a,a,a))
print(fmt0.format('b'), fmt1.format(b,b,b))
print('-'*n)
print(fmt0.format('a|b'),fmt1.format(a|b,a|b,a|b))

#XOR
print("bitwise XOR:")
print(fmt0.format('a'), fmt1.format(a,a,a))
print(fmt0.format('b'), fmt1.format(b,b,b))
print('-'*n)
print(fmt0.format('a^b'),fmt1.format(a^b,a^b,a^b))

#NOT
print("bitwise NOT:")
print(fmt0.format('a'), fmt1.format(a,a,a))
#print(fmt0.format('b'), fmt1.format(b,b,b))
print('-'*n)
#print(fmt0.format('a|b'),fmt1.format(a|b,a|b,a|b))
print(fmt0.format('~a'))

#Left Shift
print("bitwise Left Shift:")
print(fmt0.format('a'), fmt1.format(a,a,a))

print('-'*n)
print(fmt0.format('a<<2'))

#Right Shift
print("bitwise Right Shift:")
print(fmt0.format('a'), fmt1.format(a,a,a))

print('-'*n)
print(fmt0.format('a>>2'))
