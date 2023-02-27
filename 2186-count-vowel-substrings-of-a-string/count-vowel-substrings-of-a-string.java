class Solution {
 public int countVowelSubstrings(String word){int ans=0;for(int i=0;i<word.length();i++){int mask=0;for(int j=i;j<word.length();j++){int v="aeiou".indexOf(word.charAt(j));if(v<0)break; mask|=1<<v;if(mask==31)ans++;}}return ans;}
}