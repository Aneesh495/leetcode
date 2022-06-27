class Solution:
    def reformatNumber(self, number):
        s=''.join(c for c in number if c.isdigit()); out=[]
        while len(s)>4:
            out.append(s[:3]); s=s[3:]
        if len(s)==4: out.extend([s[:2],s[2:]])
        else: out.append(s)
        return '-'.join(out)