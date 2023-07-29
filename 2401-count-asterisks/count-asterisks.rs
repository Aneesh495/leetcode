impl Solution {
    pub fn count_asterisks(s: String) -> i32 {
        let mut inside_pair = false;
        let mut count = 0;
        for ch in s.chars() {
            if ch == '|' { inside_pair = !inside_pair; }
            else if ch == '*' && !inside_pair { count += 1; }
        }
        count
    }
}