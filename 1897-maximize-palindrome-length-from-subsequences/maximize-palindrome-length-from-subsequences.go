func longestPalindrome(word1 string, word2 string) int {
 s:=word1+word2;n:=len(s);dp:=make([]int,n);ans:=0
 for i:=n-1;i>=0;i-- {diag:=0;dp[i]=1;for j:=i+1;j<n;j++ {old:=dp[j];if s[i]==s[j] {dp[j]=diag+2;if i<len(word1)&&j>=len(word1)&&dp[j]>ans {ans=dp[j]}} else if dp[j-1]>dp[j] {dp[j]=dp[j-1]};diag=old}}
 return ans
}