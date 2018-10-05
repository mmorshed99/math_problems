class Solution:
    # @param A : integer
    # @return a strings
    def convertToTitle(self, A):
        import string
        def convert(num):
            count = 1
            for each_letter in string.ascii_uppercase:
                if count == num:
                    return each_letter
                count += 1
        div = A
        my_stack = []
        my_ret = ""
        temp = A
        while(div > 26):
            temp = div % 26
            if temp == 0:
                temp = 26
                div = div - 26
            my_stack.append(temp)
            div = div / 26
        my_stack.append(div)
        for i in reversed(range(len(my_stack))):
            my_ret += convert(my_stack[i])
        return my_ret
