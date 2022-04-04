class Solution {
    public double averageWaitingTime(int[][] customers) {
        long finish = 0;
        long totalWaiting = 0;
        for (int[] customer : customers) {
            // Service starts after both the customer's arrival and the prior order.
            finish = Math.max(finish, customer[0]) + customer[1];
            totalWaiting += finish - customer[0];
        }
        return (double) totalWaiting / customers.length;
    }
}