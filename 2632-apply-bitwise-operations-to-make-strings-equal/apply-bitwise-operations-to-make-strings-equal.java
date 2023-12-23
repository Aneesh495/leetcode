class Solution {
    public boolean makeStringsEqual(String s, String target) {
        // A one can create or erase other ones, but the last one cannot disappear.
        return (s.indexOf('1') >= 0) == (target.indexOf('1') >= 0);
    }
}