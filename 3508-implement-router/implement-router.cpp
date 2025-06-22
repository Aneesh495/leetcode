class Router {
    int lim;
    deque<array<int, 3>> q;
    set<array<int, 3>> st;
    unordered_map<int, deque<int>> mp;
public:
    Router(int memoryLimit) : lim(memoryLimit) {}
    bool addPacket(int source, int destination, int timestamp) {
        array<int, 3> p = {source, destination, timestamp};
        if (st.count(p)) return false;
        if ((int)q.size() == lim) forwardPacket();
        q.push_back(p);
        st.insert(p);
        mp[destination].push_back(timestamp);
        return true;
    }
    vector<int> forwardPacket() {
        if (q.empty()) return {};
        auto p = q.front(); q.pop_front();
        st.erase(p);
        mp[p[1]].pop_front();
        return {p[0], p[1], p[2]};
    }
    int getCount(int destination, int startTime, int endTime) {
        auto it = mp.find(destination);
        if (it == mp.end()) return 0;
        auto& d = it->second;
        return upper_bound(d.begin(), d.end(), endTime) - lower_bound(d.begin(), d.end(), startTime);
    }
};