func getCollisionTimes(cars [][]int) []float64 {
 n:=len(cars);ans:=make([]float64,n);stack:=[]int{}
 for i:=n-1;i>=0;i-- {ans[i]=-1;for len(stack)>0 {j:=stack[len(stack)-1];if cars[i][1]<=cars[j][1] {stack=stack[:len(stack)-1];continue};t:=float64(cars[j][0]-cars[i][0])/float64(cars[i][1]-cars[j][1]);if ans[j]<0 || t<=ans[j] {ans[i]=t;break};stack=stack[:len(stack)-1]};stack=append(stack,i)}
 return ans
}