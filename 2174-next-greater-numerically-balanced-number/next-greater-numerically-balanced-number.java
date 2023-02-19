class Solution {
 public int nextBeautifulNumber(int n) {
  for(int x=n+1;;x++){int[] c=new int[10]; int y=x; while(y>0){c[y%10]++;y/=10;} boolean ok=c[0]==0; for(int i=1;i<10;i++) if(c[i]!=0&&c[i]!=i) ok=false; if(ok)return x;}
 }
}