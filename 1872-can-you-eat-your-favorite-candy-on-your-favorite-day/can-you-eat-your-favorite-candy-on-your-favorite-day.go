func canEat(candiesCount []int, queries [][]int) []bool {
 p:=make([]int64,len(candiesCount)+1);for i,x:=range candiesCount {p[i+1]=p[i]+int64(x)}
 ans:=make([]bool,len(queries));for i,q:=range queries {t:=q[0];d:=int64(q[1])+1; cap:=int64(q[2]);ans[i]=d<=p[t+1] && d*cap>p[t]}
 return ans
}