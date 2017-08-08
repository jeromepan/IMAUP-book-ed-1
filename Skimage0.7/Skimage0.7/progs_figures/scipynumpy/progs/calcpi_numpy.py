from numpy import *
import time

def main():
    # No of terms in the series
    noofterms = 1000000
    # Calculate the denominator. 
    # First few terms are 1,3,5,7 ...
    # den is short for denominator
    den  = linspace(1,noofterms*2,noofterms)
    # Calculate the numerator. 
    # The first few terms are 1, -1, 1, -1 ...
    # num is short for numerator
    num = ones(noofterms)
    for i in range(1,noofterms):
        num[i] = pow(-1,i)
    print num
    print den
    # Find the ratio and sum all the fractions 
    # to obtain pi value
    # Start the clock
    t1 = time.clock()
    pi_value =  sum(num/den)*4.0
    print "pi_value = %f" % pi_value
    t2 = time.clock()
    # Determine the time for computation
    timetaken = t2-t1
    print "Timetaken = %f seconds" % timetaken
    
    
if __name__ == '__main__':
    main()
