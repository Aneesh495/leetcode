class Solution {
 public int countValidWords(String sentence) {
  int ans=0; for(String s: sentence.trim().split("\\s+")) {if(s.isEmpty()) continue; boolean ok=true, hy=false;
   for(int i=0;i<s.length();i++){char c=s.charAt(i); if(Character.isDigit(c)) ok=false; else if(c=='-'){if(hy||i==0||i+1==s.length()||!Character.isLowerCase(s.charAt(i-1))||!Character.isLowerCase(s.charAt(i+1))) ok=false; hy=true;} else if(!Character.isLowerCase(c)&&i!=s.length()-1) ok=false;} if(ok) ans++;
  } return ans;
 }
}