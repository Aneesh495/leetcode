
class Solution {
public:
    int findInMountainArray(int target, MountainArray &mountainArr) {
        int n = mountainArr.length();
        int l = 0, r = n - 1;
        while (l < r) {
            int mid = (l + r) / 2;
            if (mountainArr.get(mid) < mountainArr.get(mid + 1)) l = mid + 1;
            else r = mid;
        }
        int peak = l;
        int res = binSearch(mountainArr, target, 0, peak, true);
        if (res != -1) return res;
        return binSearch(mountainArr, target, peak + 1, n - 1, false);
    }
private:
    int binSearch(MountainArray &arr, int target, int l, int r, bool asc) {
        while (l <= r) {
            int mid = (l + r) / 2;
            int val = arr.get(mid);
            if (val == target) return mid;
            if (asc ? val < target : val > target) l = mid + 1;
            else r = mid - 1;
        }
        return -1;
    }
};
