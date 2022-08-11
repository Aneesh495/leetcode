func restoreArray(adjacentPairs [][]int) []int {
 g:=map[int][]int{}
 for _,p:=range adjacentPairs {a,b:=p[0],p[1];g[a]=append(g[a],b);g[b]=append(g[b],a)}
 start:=0;for x,v:=range g {if len(v)==1 {start=x;break}}
 ans:=[]int{start}; prev:=start; cur:=g[start][0]; ans=append(ans,cur)
 for len(ans)<len(g) {next:=g[cur][0];if next==prev {next=g[cur][1]};ans=append(ans,next);prev,cur=cur,next}
 return ans
}