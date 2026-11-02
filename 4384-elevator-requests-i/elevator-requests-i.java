class Solution {
    public int elevatorRequests(int n, int[] requests) {
        int position = 0;
        int time = 0;
        for (int floor : requests) {
            time += Math.abs(floor - position);
            position = floor;
        }
        return time;
    }
}