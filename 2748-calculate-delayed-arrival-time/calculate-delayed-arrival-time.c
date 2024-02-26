int findDelayedArrivalTime(int arrivalTime, int delayedTime) {
    // A full day wraps back to hour zero.
    return (arrivalTime + delayedTime) % 24;
}