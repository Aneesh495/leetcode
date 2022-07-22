class Solution:
    def largestSubmatrix(self, matrix):
        n=len(matrix[0]); heights=[0]*n; ans=0
        for row in matrix:
            heights=[h+1 if x else 0 for h,x in zip(heights,row)]
            for i,h in enumerate(sorted(heights,reverse=True),1): ans=max(ans,i*h)
        return ans