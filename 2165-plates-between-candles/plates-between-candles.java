class Solution {
 public int[] platesBetweenCandles(String s,int[][] queries) {
  int n=s.length();int[] left=new int[n],right=new int[n],pre=new int[n+1]; int p=-1;
  for(int i=0;i<n;i++){if(s.charAt(i)=='|')p=i;left[i]=p;pre[i+1]=pre[i]+(s.charAt(i)=='*'?1:0);} p=-1;for(int i=n-1;i>=0;i--){if(s.charAt(i)=='|')p=i;right[i]=p;}
  int[] ans=new int[queries.length]; for(int i=0;i<ans.length;i++){int a=right[queries[i][0]], b=left[queries[i][1]];if(a>=0&&b>a)ans[i]=pre[b]-pre[a];}return ans;
 }
}