class Solution {
    public int longestCommonSubsequence(String t1, String t2) {
        int n = t1.length();
        int m = t2.length();
        int[][] dp = new int[n+1][m+1];
        dp[0][0] = 0;

        for(int i = 1;i<=n;i++){
            for(int j=1;j<=m;j++){
                if(t1.charAt(i-1) == t2.charAt(j-1)){
                    dp[i][j] = 1 + dp[i-1][j-1];
                }else{
                    int case1 = dp[i-1][j];
                    int case2 = dp[i][j-1];
                    dp[i][j] = Math.max(case1,case2);
                }
            }
        }
        printLCS(dp,t1,t2);
        return dp[n][m];
    }

    public void printLCS(int[][] dp, String t1, String t2){
        int i = t1.length();
        int j = t2.length();
        StringBuilder sb = new StringBuilder();

        while(i > 0 && j > 0){
            if(t1.charAt(i-1) == t2.charAt(j-1)){
                sb.append(t1.charAt(i-1));
                i--; j--;
            }
            else if(dp[i-1][j] > dp[i][j-1]){
                i--;
            } else {
                j--;
            }
        }
        System.out.println(sb.reverse().toString());
    }
}