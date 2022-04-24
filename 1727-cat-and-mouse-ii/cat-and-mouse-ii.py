from collections import deque
class Solution:
    def canMouseWin(self, grid, catJump, mouseJump):
        R=len(grid); C=len(grid[0]); cells=[(r,c) for r in range(R) for c in range(C) if grid[r][c]!="#"]; ids={p:i for i,p in enumerate(cells)}; n=len(cells)
        for i,(r,c) in enumerate(cells):
            if grid[r][c]=="M": mouse=i
            elif grid[r][c]=="C": cat=i
            elif grid[r][c]=="F": food=i
        def moves(jump):
            out=[]
            for r,c in cells:
                a=[ids[r,c]]
                for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                    for d in range(1,jump+1):
                        p=(r+dr*d,c+dc*d)
                        if p not in ids: break
                        a.append(ids[p])
                out.append(a)
            return out
        mm=moves(mouseJump); cm=moves(catJump); N=n*n*2
        result=[0]*N; degree=[0]*N; dist=[0]*N; longest=[0]*N; q=deque()
        def ix(m,c,t): return (m*n+c)*2+t
        for m in range(n):
            for c in range(n):
                for t in range(2):
                    s=ix(m,c,t); degree[s]=len(mm[m]) if t==0 else len(cm[c])
                    winner=2 if m==c or c==food else (1 if m==food else 0)
                    if winner: result[s]=winner; q.append(s)
        while q:
            s=q.popleft(); t=s%2; z=s//2; m=z//n; c=z%n; winner=result[s]
            preds=( (pm,c,0) for pm in mm[m] ) if t==1 else ( (m,pc,1) for pc in cm[c] )
            for pm,pc,pt in preds:
                p=ix(pm,pc,pt)
                if result[p]: continue
                if winner==pt+1:
                    result[p]=winner; dist[p]=dist[s]+1; q.append(p)
                else:
                    degree[p]-=1; longest[p]=max(longest[p],dist[s]+1)
                    if degree[p]==0:
                        result[p]=winner; dist[p]=longest[p]; q.append(p)
        s=ix(mouse,cat,0)
        return result[s]==1 and dist[s]<=1000