class Solution {
 public String kthDistinct(String[] arr, int k) {java.util.Map<String,Integer> c=new java.util.HashMap<>(); for(String s:arr)c.merge(s,1,Integer::sum); for(String s:arr)if(c.get(s)==1&&--k==0)return s; return "";}
}