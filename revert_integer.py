#Reverse digits of an integer.
#
#Example1:
#
#x = 123,
#
#return 321
#Example2:
#
#x = -123,
#
#return -321
#
#Return 0 if the result overflows and does not fit in a 32 bit signed integer
class Solution:
    # @param A : integer
    # @return an integer
    def reverse(self, A):
        if A == 0:
            return 0
        E = abs(A)
        D = str(E)
        my_A = list(D)
        B = []
        for i in range(0, len(my_A)):
           B.append(my_A.pop())
        Q = int(''.join(map(str,B)))
        if abs(Q) > 2147483647:
            return 0
        if A < 0:
            Q = -Q
        return Q
###Should be this way##
class Solution:
    # @param A : integer
    # @return an integer
    def reverse(self, A):
        save = 0
        is_neg = 0
        if A < 0:
            is_neg = 1
        A = abs(A)
        while(A>0):
            save = (save * 10) + (A%10)
            if save > 2147483647:
                return 0
            A = A/10
        if is_neg:
            save = -save
        return save
