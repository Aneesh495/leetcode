class Solution {
 public int countHighestScoreNodes(int[] parents) {
  int n=parents.length; int[] head=new int[n],next=new int[n], order=new int[n],size=new int[n]; java.util.Arrays.fill(head,-1);
  for(int i=1;i<n;i++){next[i]=head[parents[i]];head[parents[i]]=i;} int len=1;order[0]=0; for(int i=0;i<len;i++) for(int v=head[order[i]];v!=-1;v=next[v]) order[len++]=v;
  long best=0; int count=0; for(int j=n-1;j>=0;j--){int u=order[j]; size[u]=1; long score=1; for(int v=head[u];v!=-1;v=next[v]){size[u]+=size[v];score*=size[v];} if(n-size[u]>0) score*=n-size[u]; if(score>best){best=score;count=1;}else if(score==best)count++;} return count;
 }
}