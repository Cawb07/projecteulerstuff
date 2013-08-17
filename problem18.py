'''
Created on Aug 16, 2013

https://projecteuler.net/problem=18

@author: Cawb07
'''
import time

#This function did not work in this case, but it works for smaller triangles.
'''
def greatest_path(a):
    test = 0
    
    for l in a:
        if len(l) == 1:
            pos = 0
            test += int(a[l][pos])
            print "position is " + str(pos)
            print a[l][pos]
        
        elif int(l[pos+1]) > int(a[l][pos]):
            pos = pos+1
            test += int(a[l][pos])
            print "position is " + str(pos)
            print a[l][pos]
        
        else:
            test += int(a[l][pos])
            print "position is " + str(pos)
            print a[l][pos]
    
    return test
'''
        
def greatest_path(a):
    sigma = 0
    pos = 0
    
    testpos = 0
    testpos2 = 0
    
    if len(a)%2 != 0:
        #Initializing with the tip of the triangle
        sigma += int(a[0][0])
                
        for l in range(1, len(a), 2):
            test = 0
            test2 = 0
            
            if (int(a[l][pos]) + int(a[l+1][pos])) > (int(a[l][pos]) + int(a[l+1][pos+1])):
                test += (int(a[l][pos]) + int(a[l+1][pos]))
                testpos = pos
            else:
                test += (int(a[l][pos]) + int(a[l+1][pos+1]))
                testpos = pos+1
            
            
            if (int(a[l][pos+1]) + int(a[l+1][pos+1])) > (int(a[l][pos+1]) + int(a[l+1][pos+2])):
                test2 += (int(a[l][pos+1]) + int(a[l+1][pos+1]))
                testpos2 = pos + 1
            else:
                test2 += (int(a[l][pos+1]) + int(a[l+1][pos+2]))
                testpos2 = pos+2
            
            
            if test > test2:
                pos = testpos
                sigma += test
            else:
                pos = testpos2
                sigma += test2
        
    
    else:
        for l in range(0, len(a), 2):
            test = 0
            test2 = 0
            
            if l == 0:
                if (int(a[l][l]) + int(a[l+1][l])) > (int(a[l][l]) + int(a[l+1][l+1])):
                    sigma += (int(a[l][l]) + int(a[l+1][l]))
                else:
                    sigma += (int(a[l][l]) + int(a[l+1][l+1]))
                    pos = l+1
            
            else:
                if (int(a[l][pos]) + int(a[l+1][pos])) > (int(a[l][pos]) + int(a[l+1][pos+1])):
                    test += (int(a[l][pos]) + int(a[l+1][pos]))
                    testpos = pos
                else:
                    test += (int(a[l][pos]) + int(a[l+1][pos+1]))
                    testpos = pos+1
                
                
                if (int(a[l][pos+1]) + int(a[l+1][pos+1])) > (int(a[l][pos+1]) + int(a[l+1][pos+2])):
                    test2 += (int(a[l][pos+1]) + int(a[l+1][pos+1]))
                    testpos2 = pos + 1
                else:
                    test2 += (int(a[l][pos+1]) + int(a[l+1][pos+2]))
                    testpos2 = pos+2
                
                
                if test > test2:
                    pos = testpos
                    sigma += test
                else:
                    pos = testpos2
                    sigma += test2
    
    return sigma



start = time.time()

rows = [line.split(' ') for line in open('./small_triangle.txt')]
print greatest_path(rows)

elapsed = time.time() - start
print "The elapsed time is %s seconds." % (elapsed)