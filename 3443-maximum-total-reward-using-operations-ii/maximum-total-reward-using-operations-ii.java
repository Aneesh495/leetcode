import java.util.Arrays;

class Solution {
    public int maxTotalReward(int[] rewardValues) {
        Arrays.sort(rewardValues);
        int maxBits = 100_001;
        long[] reachable = new long[(maxBits + 63) / 64];
        reachable[0] = 1L;

        int previous = -1;
        for (int reward : rewardValues) {
            if (reward == previous) continue;
            previous = reward;
            int lastSourceWord = (reward - 1) >>> 6;
            int wordShift = reward >>> 6;
            int bitShift = reward & 63;
            int remainder = reward & 63;

            for (int word = lastSourceWord; word >= 0; word--) {
                long source = reachable[word];
                if (word == lastSourceWord && remainder != 0) {
                    source &= (1L << remainder) - 1;
                }
                if (source == 0) continue;
                int dest = word + wordShift;
                if (dest < reachable.length) reachable[dest] |= source << bitShift;
                if (bitShift != 0 && dest + 1 < reachable.length) {
                    reachable[dest + 1] |= source >>> (64 - bitShift);
                }
            }
        }

        for (int word = reachable.length - 1; word >= 0; word--) {
            if (reachable[word] != 0) {
                return word * 64 + 63 - Long.numberOfLeadingZeros(reachable[word]);
            }
        }
        return 0;
    }
}