
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = {}
        rank = {}
        email_to_name = {}

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a, b):
            ra, rb = find(a), find(b)
            if ra == rb:
                return
            if rank[ra] < rank[rb]:
                parent[ra] = rb
            elif rank[ra] > rank[rb]:
                parent[rb] = ra
            else:
                parent[rb] = ra
                rank[ra] += 1

        for acc in accounts:
            name = acc[0]
            for email in acc[1:]:
                if email not in parent:
                    parent[email] = email
                    rank[email] = 0
                    email_to_name[email] = name
            root = acc[1]
            for email in acc[2:]:
                union(root, email)

        groups = defaultdict(list)
        for email in parent:
            groups[find(email)].append(email)

        res = []
        for root, emails in groups.items():
            res.append([email_to_name[root]] + sorted(set(emails)))
        return res
