func closestCost(baseCosts []int, toppingCosts []int, target int) int {
 best:=baseCosts[0];abs:=func(x int)int{if x<0{return -x};return x}
 var dfs func(int,int);dfs=func(i,sum int) {if abs(sum-target)<abs(best-target) || (abs(sum-target)==abs(best-target)&&sum<best) {best=sum};if i==len(toppingCosts)||sum>=target {return};for k:=0;k<=2;k++ {dfs(i+1,sum+k*toppingCosts[i])}}
 for _,b:=range baseCosts {dfs(0,b)};return best
}