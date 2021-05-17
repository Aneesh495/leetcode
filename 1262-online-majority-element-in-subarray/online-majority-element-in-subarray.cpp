
#include <bits/stdc++.h>
using namespace std;

class MajorityChecker {
    // Segment tree node stores a candidate value and its balance
    struct Node {
        int cand;   // candidate value
        int bal;    // balance count from Boyer Moore merge
    };

    int n;
    vector<int> arr;
    vector<Node> seg;
    unordered_map<int, vector<int>> pos; // value -> sorted indices

    // Merge two nodes using Boyer Moore idea
    Node mergeNode(const Node& a, const Node& b) {
        Node res;
        if (a.cand == b.cand) {
            res.cand = a.cand;
            res.bal = a.bal + b.bal;
        } else if (a.bal > b.bal) {
            res.cand = a.cand;
            res.bal = a.bal - b.bal;
        } else {
            res.cand = b.cand;
            res.bal = b.bal - a.bal;
        }
        return res;
    }

    void build(int idx, int l, int r) {
        if (l == r) {
            seg[idx] = {arr[l], 1};
            return;
        }
        int m = (l + r) >> 1;
        build(idx << 1, l, m);
        build(idx << 1 | 1, m + 1, r);
        seg[idx] = mergeNode(seg[idx << 1], seg[idx << 1 | 1]);
    }

    Node queryNode(int idx, int l, int r, int ql, int qr) {
        if (ql <= l && r <= qr) return seg[idx];
        int m = (l + r) >> 1;
        if (qr <= m) return queryNode(idx << 1, l, m, ql, qr);
        if (ql > m)  return queryNode(idx << 1 | 1, m + 1, r, ql, qr);
        Node left = queryNode(idx << 1, l, m, ql, qr);
        Node right = queryNode(idx << 1 | 1, m + 1, r, ql, qr);
        return mergeNode(left, right);
    }

    // count occurrences of val in [l, r] using precomputed positions
    int countInRange(int val, int l, int r) {
        const auto& v = pos[val];
        auto it1 = lower_bound(v.begin(), v.end(), l);
        auto it2 = upper_bound(v.begin(), v.end(), r);
        return int(it2 - it1);
    }

public:
    MajorityChecker(vector<int>& arrIn) {
        arr = arrIn;
        n = int(arr.size());
        seg.assign(4 * max(1, n), {0, 0});
        for (int i = 0; i < n; ++i) pos[arr[i]].push_back(i);
        if (n > 0) build(1, 0, n - 1);
    }

    int query(int left, int right, int threshold) {
        // get candidate by Boyer Moore on the range
        Node candNode = queryNode(1, 0, n - 1, left, right);
        int cand = candNode.cand;
        // verify frequency using positions
        int cnt = countInRange(cand, left, right);
        if (cnt >= threshold) return cand;
        return -1;
    }
};
