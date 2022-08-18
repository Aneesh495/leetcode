func check(nums []int) bool {
 drops:=0;for i,x:=range nums {if x>nums[(i+1)%len(nums)] {drops++}};return drops<=1
}