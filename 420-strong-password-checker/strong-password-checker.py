
class Solution:
    def strongPasswordChecker(self, password: str) -> int:
        n = len(password)

        # 1. Check missing character types
        has_lower = any(c.islower() for c in password)
        has_upper = any(c.isupper() for c in password)
        has_digit = any(c.isdigit() for c in password)
        missing = int(not has_lower) + int(not has_upper) + int(not has_digit)

        # 2. Collect lengths of repeating runs of the same character
        runs = []
        i = 0
        while i < n:
            j = i
            while j < n and password[j] == password[i]:
                j += 1
            run_len = j - i
            if run_len >= 3:
                runs.append(run_len)
            i = j

        # Helper to compute replacements needed given run lengths
        def replacements_needed(runs_list):
            return sum(l // 3 for l in runs_list)

        # Case A. If length is less than 6
        # We need insertions to reach length 6
        # Insertions can also fix missing types and can split repeats
        if n < 6:
            return max(missing, 6 - n, replacements_needed(runs))

        # Case B. If length is between 6 and 20
        # Only replacements for repeats and missing types matter
        if n <= 20:
            return max(missing, replacements_needed(runs))

        # Case C. If length is greater than 20
        # We must delete characters. Deletions can reduce needed replacements for repeats.
        deletions = n - 20

        # Count how many runs fall into each modulo-3 bucket
        # A run of length L needs L//3 replacements
        # Deleting 1 character from a run with L%3==0 reduces one replacement need
        # Deleting 2 characters from a run with L%3==1 reduces one replacement need
        # Deleting 3 characters from any run reduces one replacement need
        mod_cnt = [0, 0, 0]
        for l in runs:
            mod_cnt[l % 3] += 1

        reps = replacements_needed(runs)

        # Use deletions greedily to reduce replacements
        # First consume runs where 1 deletion saves 1 replacement
        use = min(mod_cnt[0], deletions)
        reps -= use
        deletions -= use

        # Next consume runs where 2 deletions save 1 replacement
        use = min(mod_cnt[1] * 2, deletions)
        reps -= use // 2
        deletions -= use

        # Finally every 3 deletions save 1 replacement
        reps -= deletions // 3
        # No need to update deletions further since we only care about total edits

        # Total edits equal required deletions plus the max of remaining replacements and missing types
        return (n - 20) + max(missing, reps)
