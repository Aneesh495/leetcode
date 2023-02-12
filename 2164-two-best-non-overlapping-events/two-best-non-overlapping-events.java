class Solution {
 public int maxTwoEvents(int[][] events) {
  java.util.Arrays.sort(events,(a,b)->Integer.compare(a[1],b[1])); int n=events.length,ans=0; int[] best=new int[n+1];
  for(int i=0;i<n;i++){int l=0,r=i; while(l<r){int m=(l+r)/2; if(events[m][1]<events[i][0]) l=m+1; else r=m;} ans=Math.max(ans,events[i][2]+best[l]); best[i+1]=Math.max(best[i],events[i][2]);} return ans;
 }
}