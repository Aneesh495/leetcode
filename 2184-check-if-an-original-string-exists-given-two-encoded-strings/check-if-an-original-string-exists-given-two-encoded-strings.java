class Solution {
 String a,b; java.util.Set<String> seen=new java.util.HashSet<>();
 public boolean possiblyEquals(String s1,String s2){a=s1;b=s2;return dfs(0,0,0);}
 boolean dfs(int i,int j,int d){
  if(i==a.length()&&j==b.length())return d==0; String key=i+","+j+","+d;if(!seen.add(key))return false;
  int v=0;for(int p=i;p<a.length()&&Character.isDigit(a.charAt(p));p++){v=v*10+a.charAt(p)-'0';if(dfs(p+1,j,d+v))return true;}
  v=0;for(int p=j;p<b.length()&&Character.isDigit(b.charAt(p));p++){v=v*10+b.charAt(p)-'0';if(dfs(i,p+1,d-v))return true;}
  if(d<0&&i<a.length()&&Character.isLetter(a.charAt(i))&&dfs(i+1,j,d+1))return true;
  if(d>0&&j<b.length()&&Character.isLetter(b.charAt(j))&&dfs(i,j+1,d-1))return true;
  return d==0&&i<a.length()&&j<b.length()&&Character.isLetter(a.charAt(i))&&a.charAt(i)==b.charAt(j)&&dfs(i+1,j+1,0);
 }
}