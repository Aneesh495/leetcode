class Bitset {
private:
    vector<bool> bits;
    bool flipped = false;
    int ones = 0;
public:
    Bitset(int size) : bits(size, false) {}

    void fix(int idx) {
        if (!(bits[idx] ^ flipped)) {
            bits[idx] = !flipped;
            ++ones;
        }
    }

    void unfix(int idx) {
        if (bits[idx] ^ flipped) {
            bits[idx] = flipped;
            --ones;
        }
    }

    void flip() {
        flipped = !flipped;
        ones = static_cast<int>(bits.size()) - ones;
    }

    bool all() { return ones == static_cast<int>(bits.size()); }
    bool one() { return ones > 0; }
    int count() { return ones; }

    string toString() {
        string result;
        result.reserve(bits.size());
        for (bool bit : bits) result.push_back((bit ^ flipped) ? '1' : '0');
        return result;
    }
};