func countBalls(lowLimit int, highLimit int) int {
 counts:=make([]int,46); best:=0
 for x:=lowLimit;x<=highLimit;x++ {sum:=0; for y:=x;y>0;y/=10 {sum+=y%10}; counts[sum]++; if counts[sum]>best {best=counts[sum]}}
 return best
}