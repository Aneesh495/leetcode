class Solution {
public:
    int minRange(int a, int b, int c) {
        int v[3] = {a, b, c};
        sort(v, v + 3);
        return min(v[2] - v[0], v[1]);
    }
};