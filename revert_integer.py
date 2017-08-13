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
