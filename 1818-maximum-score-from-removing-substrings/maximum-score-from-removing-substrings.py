class Solution:
    def maximumGain(self, s, x, y):
        first,second=('ab','ba') if x>=y else ('ba','ab')
        def remove(s,p,score):
            stack=[]; total=0
            for c in s:
                if stack and stack[-1]==p[0] and c==p[1]: stack.pop(); total+=score
                else: stack.append(c)
            return stack,total
        rest,a=remove(s,first,max(x,y)); _,b=remove(rest,second,min(x,y))
        return a+b