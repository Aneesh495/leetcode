class Solution {
    using i64 = long long;

    // Count set bits and sum their positions across the integers in [0, end).
    pair<i64, i64> bitTotals(i64 end) {
        i64 count = 0, exponent = 0;
        for (int bit = 0; (1LL << bit) < end; ++bit) {
            i64 half = 1LL << bit;
            i64 period = 2 * half;
            i64 ones = end / period * half + max(0LL, end % period - half);
            count += ones;
            exponent += ones * bit;
        }
        return {count, exponent};
    }

    i64 prefixExponent(i64 length) {
        i64 left = 1, right = length + 1;
        while (left < right) {
            i64 mid = left + (right - left + 1) / 2;
            if (bitTotals(mid).first <= length) left = mid;
            else right = mid - 1;
        }
        auto [count, exponent] = bitTotals(left);
        // The unfinished integer contributes its lowest set bits first.
        for (int bit = 0; count < length; ++bit) {
            if (left & (1LL << bit)) {
                ++count;
                exponent += bit;
            }
        }
        return exponent;
    }

    int powerOfTwo(i64 exponent, i64 mod) {
        i64 answer = 1 % mod, base = 2 % mod;
        for (; exponent > 0; exponent >>= 1) {
            if (exponent & 1) answer = answer * base % mod;
            base = base * base % mod;
        }
        return static_cast<int>(answer);
    }

public:
    vector<int> findProductsOfElements(vector<vector<long long>>& queries) {
        vector<int> answer;
        answer.reserve(queries.size());
        for (const auto& query : queries) {
            i64 exponent = prefixExponent(query[1] + 1) - prefixExponent(query[0]);
            answer.push_back(powerOfTwo(exponent, query[2]));
        }
        return answer;
    }
};