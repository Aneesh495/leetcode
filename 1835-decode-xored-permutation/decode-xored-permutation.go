func decode(encoded []int) []int {
 n:=len(encoded)+1; first:=0
 for i:=1;i<=n;i++ {first ^= i}
 for i:=1;i<len(encoded);i+=2 {first ^= encoded[i]}
 ans:=make([]int,n); ans[0]=first
 for i,x:=range encoded {ans[i+1]=ans[i]^x}
 return ans
}