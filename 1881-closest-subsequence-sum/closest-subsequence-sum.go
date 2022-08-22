import "sort"
func minAbsDifference(nums []int, goal int) int {
 sums:=func(a []int) []int {r:=[]int{0};for _,v:=range a {n:=len(r);for i:=0;i<n;i++ {r=append(r,r[i]+v)}};return r}
 left:=sums(nums[:len(nums)/2]);right:=sums(nums[len(nums)/2:]);sort.Ints(right);best:=int(^uint(0)>>1)
 for _,x:=range left {target:=goal-x;i:=sort.SearchInts(right,target);if i<len(right) {d:=right[i]-target;if d<best {best=d}};if i>0 {d:=target-right[i-1];if d<best {best=d}};if best==0{return 0}}
 return best
}