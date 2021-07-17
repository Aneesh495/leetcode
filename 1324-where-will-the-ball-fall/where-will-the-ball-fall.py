class Solution:
    def findBall(self, grid):
        n=len(grid[0]); ans=[]
        for start in range(n):
            col=start
            for row in grid:
                nxt=col+row[col]
                if nxt<0 or nxt>=n or row[nxt]!=row[col]:
                    col=-1; break
                col=nxt
            ans.append(col)
        return ans