class Solution {
 public boolean checkAlmostEquivalent(String word1,String word2){int[] c=new int[26];for(char x:word1.toCharArray())c[x-'a']++;for(char x:word2.toCharArray())c[x-'a']--;for(int v:c)if(Math.abs(v)>3)return false;return true;}
}