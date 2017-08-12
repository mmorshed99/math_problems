#Given a positive integer which fits in a 32 bit signed integer, find if it can be expressed as A^P where P > 1 and A > 0. A and P both should be integers.
#
#Example
#
#Input : 4
#Output : True  
#as 2^2 = 4. 
#
#use math to obtain fractional powers of 1/2, 1/3, 1/4, and so on, up to 1/log2 n. 
#The result would be an A; the denominator of the fraction would be P.
#need to try both ceil and floor of the result.
#
class Solution:
    # @param A : integer
    # @return an integer
    def isPower(self, A):
        max = math.log(A,2)
        max = math.floor(max)
        if A == 1:
            return 1
        for i in range(2,max+1):
           x = A**(1/i)
           if math.floor(x) ** i == A:
              return 1
           if math.ceil(x) ** i == A:
              return 1          
        return 0
