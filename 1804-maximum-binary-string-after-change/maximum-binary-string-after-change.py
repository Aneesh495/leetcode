class Solution:
    def maximumBinaryString(self, binary):
        z=binary.count('0')
        if not z: return binary
        i=binary.index('0')+z-1
        return '1'*i+'0'+'1'*(len(binary)-i-1)