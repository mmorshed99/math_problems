class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def uniquePaths(self, A, B):
        def find(x,y):
            if x < 0 or y < 0 or x > A-1 or y > B-1:
                return 0
            if save[x][y] != -1:
                return save[x][y]
            if x == A-1 and y == B-1:
                return 1
            save[x][y] = find(x+1,y) + find(x,y+1)
            return save[x][y]
        import sys
        sys.setrecursionlimit(30000)
        save = []
        for i in range(A):
            save.append([])
            for j in range(B):
                save[i].append(-1)
        return find(0,0)
