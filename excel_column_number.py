#Given a column title as appears in an Excel sheet, return its corresponding column number.
#
#Example:
#
#    A -> 1
#    
#    B -> 2
#    
#    C -> 3
#
class Solution:
    # @param A : string
    # @return an integer
    def titleToNumber(self, A):
        import string
        letters = {}
        i =	1
        for	key in string.ascii_uppercase:
            letters[key] = i
            i = i+1
        column_name	= list(A)    
        column_number = 0 
        for	i in range(0,len(column_name)):
            j = abs(len(column_name)-i-1)
            column_number += letters[column_name[i]] * math.pow(26,j)
        return int(column_number)    
