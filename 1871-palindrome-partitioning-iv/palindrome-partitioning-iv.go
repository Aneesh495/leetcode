func checkPartitioning(s string) bool {
 n:=len(s); p:=make([][]bool,n);for i:=range p {p[i]=make([]bool,n)}
 for i:=n-1;i>=0;i-- {for j:=i;j<n;j++ {p[i][j]=s[i]==s[j] && (j-i<2 || p[i+1][j-1])}}
 for i:=1;i<n-1;i++ {if p[0][i-1] {for j:=i+1;j<n;j++ {if p[i][j-1] && p[j][n-1] {return true}}}}
 return false
}