'''
Created on Jul 1, 2013

projecteuler.net/problem=3

@author: Cawb07
'''

def check_factors(y):
    if (y%2 == 0):
        x = y / 2
        print "2 is true"
        print x
    
    if (y%3 == 0):
        x = y / 3
        print "3 is true"
        print x
        
    if (y%5 == 0):
        x = y / 5
        print "5 is true"
        print x
        
    if (y%7 == 0):
        x = y / 7
        print "7 is true"
        print x
        
    if (y%11 == 0):
        x = y / 11
        print "11 is true"
        print x
        
    if (y%13 == 0):
        x = y / 13
        print "13 is true"
        print x
        
    if (y%17 == 0):
        x = y / 17
        print "17 is true"
        print x
        
    for x in range(1,10000):
        if (x != 1 and x%2 != 0 and x%3 != 0 and x%5 != 0 
            and x%7 != 0 and x%11 != 0 and x%13 != 0 
            and x%17 != 0 and x%19 != 0 and x%23 != 0
            and x%29 != 0 and x%31 != 0 and x%37 != 0
            and x%41 != 0 and x%43 != 0 and x%47 != 0
            and x%53 != 0 and x%59 != 0 and x%61 != 0
            and x%67 != 0 and x%73 != 0 and x%79 != 0
            and x%83 != 0 and x%89 != 0 and x%97 != 0
            and y%x == 0):
                z = y / x
                print "%d is true" % (x)
                print z
                
    #for x in range(1,100):
        #if (x != 1 and x%2 != 0 and x%3 != 0 and x%5 != 0 
            #and x%7 != 0 and x%11 != 0 and x%13 != 0 
            #and x%17 != 0 and x%19 != 0 and x%23 != 0
            #and x%29 != 0 and x%31 != 0 and x%37 != 0):
            #print x
        
check_factors(600851475143)
check_factors(13195)
