## finding square root optimally
class Solution:
    # @param A : integer
    # @return an integer
    a = 0
    n = 0
    def sqrt(self, A):
        if self.a == A: return self.n
        else: self.a=A
        mid = 1
        lo = 1
        hi = A
        while lo < hi:
            mid = lo + (hi-lo)//2
            midval = mid*mid
           # print midval, self.n
            if midval < A:
                lo = mid+1
            elif midval > A: 
                hi = mid
            else:
                return mid
                
        if mid*mid>A: mid-=1
        self.n = mid
        return mid
       # print "!!!", lo, hi, mid 
        return mid
