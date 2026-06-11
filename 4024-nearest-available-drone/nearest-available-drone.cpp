class Solution {
public:
    int nearestDrone(vector<vector<int>>& drones, vector<int>& target) {
        int bestIndex = -1, bestDistance = INT_MAX;
        for (int i = 0; i < drones.size(); ++i) {
            int distance = abs(drones[i][0] - target[0]) + abs(drones[i][1] - target[1]);
            // Only strict improvements replace the earliest index of a tie.
            if (distance <= drones[i][2] && distance < bestDistance) {
                bestDistance = distance;
                bestIndex = i;
            }
        }
        return bestIndex;
    }
};