class Spreadsheet {
    unordered_map<string, int> mp;
    int getVal(const string& s) {
        if (isdigit(s[0])) return stoi(s);
        auto it = mp.find(s);
        return it == mp.end() ? 0 : it->second;
    }
public:
    Spreadsheet(int rows) {}
    void setCell(string cell, int value) { mp[cell] = value; }
    void resetCell(string cell) { mp.erase(cell); }
    int getValue(string formula) {
        size_t plus = formula.find('+');
        return getVal(formula.substr(1, plus - 1)) + getVal(formula.substr(plus + 1));
    }
};