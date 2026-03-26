#data_types.py
a = 10  #int
b = 3.14 # float\
c = "Hello" #str
d = True # bool
print(f"{a} is a {type(a)}\n{b} is a {type(b)}\n{c} is a {type(c)}\n{d} is a {type(d)} ")

#print(f"{a} is a {type(a)}")
#print(f"{b} is a {type(b)}")
#print(f"{c} is a {type(c)}")
#print(f"{d} is a {type(d)}")


#string
e = 'shant'
f = "bhar"
name = e + " " + f
g = name + " said, \" It's a beautiful day!"
h ='"how \' ya doin\' today?\n\t"good!"'

print(g , "\n",h)

i = True
j = False
k = bool(-1)
l = bool(a)
m = bool("")
n = bool(0)
o = bool(g)

print(i,j,k,l,m,n,o)