
class Solution {
public:
    vector<double> sampleStats(vector<int>& count) {
        double minVal = -1, maxVal = -1, mean = 0, median = 0, mode = 0;
        long long total = 0, sum = 0, maxCount = 0;
        for (int i = 0; i < 256; ++i) {
            if (count[i] > 0) {
                if (minVal == -1) minVal = i;
                maxVal = i;
                sum += (long long)i * count[i];
                total += count[i];
                if (count[i] > maxCount) {
                    maxCount = count[i];
                    mode = i;
                }
            }
        }
        mean = (double)sum / total;
        long long mid1 = (total + 1) / 2, mid2 = (total % 2 == 0) ? mid1 + 1 : mid1, cnt = 0;
        double m1 = -1, m2 = -1;
        for (int i = 0; i < 256; ++i) {
            cnt += count[i];
            if (m1 == -1 && cnt >= mid1) m1 = i;
            if (cnt >= mid2) { m2 = i; break; }
        }
        median = (m1 + m2) / 2.0;
        return {minVal, maxVal, mean, median, mode};
    }
};
