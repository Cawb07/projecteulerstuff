'''
Created on Jul 2, 2013

projecteuler.net/problem=4

@author: Cawb07
'''


for a in range(900, 1000):
    for b in range(900, 1000):
        x = a*b
        y = str(x)
        z = []
        for digit in y:
            z.append(int(digit))
        if(z[0] == z[len(z)-1] 
           and z[1] == z[len(z)-2] and z[2] == z[len(z)-3]):
            print z


'''
x = 91*99
y = str(x)
z = []
for digit in y:
    z.append(int(digit))
print z
print len(z)
print z[0]
print z[len(z)-1]
'''