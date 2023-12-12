class DataStream {
    private final int value;
    private final int k;
    private int trailingMatches = 0;

    public DataStream(int value, int k) {
        this.value = value;
        this.k = k;
    }

    public boolean consec(int num) {
        if (num == value) trailingMatches++;
        else trailingMatches = 0;
        return trailingMatches >= k;
    }
}