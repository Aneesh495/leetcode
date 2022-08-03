import "sort"
func kthLargestValue(matrix [][]int, k int) int {
 m,n:=len(matrix),len(matrix[0]); prev:=make([]int,n+1); vals:=make([]int,0,m*n)
 for _,row:=range matrix {cur:=make([]int,n+1); for j,x:=range row {cur[j+1]=x^cur[j]^prev[j+1]^prev[j]; vals=append(vals,cur[j+1])}; prev=cur}
 sort.Ints(vals); return vals[len(vals)-k]
}