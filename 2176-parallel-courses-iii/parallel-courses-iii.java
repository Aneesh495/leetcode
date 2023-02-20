class Solution {
 public int minimumTime(int n, int[][] relations, int[] time) {
  int[] head=new int[n],next=new int[relations.length],to=new int[relations.length],ind=new int[n],finish=new int[n],q=new int[n]; java.util.Arrays.fill(head,-1);
  for(int i=0;i<relations.length;i++){int u=relations[i][0]-1,v=relations[i][1]-1; to[i]=v;next[i]=head[u];head[u]=i;ind[v]++;}
  int l=0,r=0,ans=0;for(int i=0;i<n;i++) if(ind[i]==0){q[r++]=i; finish[i]=time[i];}
  while(l<r){int u=q[l++];ans=Math.max(ans,finish[u]); for(int e=head[u];e!=-1;e=next[e]){int v=to[e];finish[v]=Math.max(finish[v],finish[u]+time[v]);if(--ind[v]==0)q[r++]=v;}} return ans;
 }
}