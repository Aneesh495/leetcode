class Solution {
    public boolean hasAllCodes(String s, int k) {
        int required=1<<k;
        if (s.length()-k+1 < required) return false;
        boolean[] seen=new boolean[required];
        int mask=0, count=0;
        for (int i=0;i<s.length();i++) {
            mask=((mask<<1)&(required-1)) | (s.charAt(i)-'0');
            if (i>=k-1 && !seen[mask]) { seen[mask]=true; count++; }
        }
        return count==required;
    }
}