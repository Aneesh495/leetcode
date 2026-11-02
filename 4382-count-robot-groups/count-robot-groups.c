int countGroups(int* position, int positionSize, int* speed, int speedSize, int distance) {
    int groups = 0;
    int nextFinalSpeed = 0;
    for (int i = positionSize - 1; i >= 0; --i) {
        // At time zero only the rightmost robot of each touching block survives as leader.
        if (i + 1 < positionSize && position[i + 1] - position[i] <= distance) continue;
        // After time zero a group can only slow down. Faster trailing leaders eventually catch up.
        if (groups == 0 || speed[i] <= nextFinalSpeed) {
            ++groups;
            nextFinalSpeed = speed[i];
        }
    }
    return groups;
}