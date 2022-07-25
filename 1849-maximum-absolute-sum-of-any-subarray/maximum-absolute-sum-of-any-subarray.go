func maxAbsoluteSum(nums []int) int {
 s,lo,hi:=0,0,0
 for _,x:=range nums {s+=x;if s<lo {lo=s};if s>hi {hi=s}}
 return hi-lo
}