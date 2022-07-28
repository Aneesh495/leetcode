import "sort"
func maxValue(events [][]int, k int) int {
 sort.Slice(events,func(i,j int)bool{return events[i][0]<events[j][0]}); n:=len(events); next:=make([]int,n)
 for i,e:=range events {end:=e[1];next[i]=sort.Search(n,func(j int)bool{return events[j][0]>end})}
 prev:=make([]int,n+1)
 for t:=1;t<=k;t++ {cur:=make([]int,n+1);for i:=n-1;i>=0;i-- {take:=events[i][2]+prev[next[i]];cur[i]=cur[i+1];if take>cur[i] {cur[i]=take}};prev=cur}
 return prev[0]
}