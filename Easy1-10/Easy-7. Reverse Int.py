# Given a 32-bit signed integer, reverse digits of an integer.

## Note:
## Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. 
## For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

##submission 1
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign=1
        if x<0:
            x=-x
            sign=-1

        
        string = str(x)
        reverse_int=0
        for i in range(len(string)):
            reverse_int += int(string[i])*10**i 
            
        if x>=2**31-1 or reverse_int>=2**31-1:
            return 0
        return sign*reverse_int
            
## beat 14%

#######some great solutions ###################

##1 credit to StefanPochmann
## python 2
def reverse(self, x):
    s = cmp(x, 0)
    r = int(`s*x`[::-1])
    return s*r * (r < 2**31)

## cmp(x,y) => if x < y return -1, if x == y return 0, if x > y return 1。
## As compressed one-liner, for potential comparison:

def reverse(self, x):
    s=cmp(x,0);r=int(`s*x`[::-1]);return(r<2**31)*s*r
    
## python3

def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = lambda x: x and (1, -1)[x < 0]
        r = int(str(sign(x)*x)[::-1])
        return (sign(x)*r, 0)[r > 2**31 - 1]
        
############              ##############       
###inspired by discussion, here is the submission 2
##submission2

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign=1
        if x<0:
            x=-x
            sign=-1

        
        string = str(x)
        reverse_int=int(string[::-1])
        
        #if x>=2**31-1 or reverse_int>=2**31-1:
         #   return 0
        return sign*reverse_int*(x<2**31 and reverse_int<2**31)
#beat 85%!!!

##conclusion
##[::-1] function
##multiply true and false
