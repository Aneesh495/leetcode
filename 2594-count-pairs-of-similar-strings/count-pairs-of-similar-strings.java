class Solution {
    public int similarPairs(String[] words) {
        Map<Integer, Integer> counts = new HashMap<>();
        int pairs = 0;
        for (String word : words) {
            int mask = 0;
            for (char c : word.toCharArray()) {
                mask |= 1 << (c - 'a');
            }
            int seen = counts.getOrDefault(mask, 0);
            pairs += seen;
            counts.put(mask, seen + 1);
        }
        return pairs;
    }
}