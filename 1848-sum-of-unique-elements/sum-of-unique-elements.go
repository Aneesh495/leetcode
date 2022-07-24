func sumOfUnique(nums []int) int {
 c:=map[int]int{};for _,x:=range nums {c[x]++}; ans:=0;for x,n:=range c {if n==1 {ans+=x}};return ans
}