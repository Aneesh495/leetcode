import heapq
class Solution:
    def eatenApples(self, apples, days):
        h=[]; day=ans=0
        while day<len(apples) or h:
            if day<len(apples) and apples[day]: heapq.heappush(h,[day+days[day],apples[day]])
            while h and h[0][0]<=day: heapq.heappop(h)
            if h:
                h[0][1]-=1; ans+=1
                if not h[0][1]: heapq.heappop(h)
            day+=1
        return ans