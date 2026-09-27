class Solution {
public:
    vector<double> internalAngles(vector<int>& sides) {
        sort(sides.begin(), sides.end());
        if (sides[0] + sides[1] <= sides[2]) return {};
        vector<double> result;
        for (int i = 0; i < 3; ++i) {
            double a = sides[i], b = sides[(i+1)%3], c = sides[(i+2)%3];
            // Angles are ordered by the lengths of their opposite sides.
            double cosine = (b*b + c*c - a*a) / (2*b*c);
            result.push_back(acos(clamp(cosine, -1.0, 1.0)) * 180.0 / acos(-1.0));
        }
        return result;
    }
};