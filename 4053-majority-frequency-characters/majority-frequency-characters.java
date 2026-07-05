class Solution {
    public String majorityFrequencyGroup(String s) {
        int[] charFrequency = new int[26];
        for (char c : s.toCharArray()) charFrequency[c - 'a']++;

        int[] groupSize = new int[s.length() + 1];
        for (int frequency : charFrequency) {
            if (frequency > 0) groupSize[frequency]++;
        }

        int bestFrequency = 0;
        int largestGroup = 0;
        for (int frequency = 1; frequency <= s.length(); frequency++) {
            if (groupSize[frequency] > largestGroup ||
                (groupSize[frequency] == largestGroup && frequency > bestFrequency)) {
                largestGroup = groupSize[frequency];
                bestFrequency = frequency;
            }
        }

        StringBuilder answer = new StringBuilder();
        for (int i = 0; i < 26; i++) {
            if (charFrequency[i] == bestFrequency) answer.append((char) ('a' + i));
        }
        return answer.toString();
    }
}