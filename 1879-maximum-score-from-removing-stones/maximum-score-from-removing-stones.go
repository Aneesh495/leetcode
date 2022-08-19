func maximumScore(a int,b int,c int) int {
 total:=a+b+c; largest:=a;if b>largest {largest=b};if c>largest {largest=c};if total-largest<total/2 {return total-largest};return total/2
}