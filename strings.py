S = 'shrubbery'
# Expand String to a list
L = list(S)

print(L)

L[1] = 'c'
print(L)

print(''.join(L))

# Using bytearray
B = bytearray(b'spam')
B.extend(b'eggs')
print(B)
print(B.decode())

C = bytearray(b'test')
print(C.decode())

S2 = 'spam'
print(S2.find('pa'))
print(S2.replace('sp', 'd') + 'n')

alphabet = 'a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z'
print(alphabet.split())
print(alphabet[-1])

print(S2.upper())
print(S2.isalpha()) #isdigit()

new = ''.join(alphabet) + ' '  + ' 123'
print(new)
print(new.split())

real = 'real'
really = real.__add__('ly') # call for + , concatenation
print(real) # strings are immutable, real is still 'real'
print(really)


