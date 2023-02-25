class Solution {
 public int minimumOperations(int[] nums, int start, int goal) {
  int[] dist=new int[1001],q=new int[1001];java.util.Arrays.fill(dist,-1);int l=0,r=0;q[r++]=start;dist[start]=0;
  while(l<r){int x=q[l++];if(x==goal)return dist[x];for(int a:nums)for(int y:new int[]{x+a,x-a,x^a}){if(y==goal)return dist[x]+1;if(y>=0&&y<=1000&&dist[y]<0){dist[y]=dist[x]+1;q[r++]=y;}}}return -1;
 }
}