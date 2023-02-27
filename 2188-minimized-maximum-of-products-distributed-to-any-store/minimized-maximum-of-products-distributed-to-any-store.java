class Solution {
 public int minimizedMaximum(int n,int[] quantities){int l=1,r=100000;while(l<r){int m=l+(r-l)/2;long stores=0;for(int x:quantities) stores+=(x+m-1)/m;if(stores<=n)r=m;else l=m+1;}return l;}
}