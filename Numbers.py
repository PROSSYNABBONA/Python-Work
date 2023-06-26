#Numbers
#intergers,floats,complex
w=10#int
r=3.6#float
s=2j#complex

print(type(w))
print(type(r))
print(type(r))

#intergers
a=2
b=3456
c=-23442
print(type(a))
print(type(b))
print(type(c))

#floats
q=2.45
z=3.8
f=-78.8
print(type(q))
print(type(z))
print(type(f))

#complex numbers
s=2+10j
t=4j
h=-2j
print(type(s))
print(type(t))
print(type(h))

#Type conversion
#convert from int to complex
z=complex(w)
print(z)
print(type(z))
#convert from int to float
d=float(w)
print(d)
print(type(d))
#convert from float to complex
k=complex(q)
print(k)
print(type(k))
#convert from complex to float
t =  1+4j
h = t.real#real used to convert complex number to a float
print(h)
print(type(h))