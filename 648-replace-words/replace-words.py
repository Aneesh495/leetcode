
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = {}
        END = "#"
        for root in dictionary:
            node = trie
            for ch in root:
                node = node.setdefault(ch, {})
            node[END] = True

        def replace(word: str) -> str:
            node = trie
            prefix = []
            for ch in word:
                if END in node:
                    return "".join(prefix)
                if ch not in node:
                    return word
                node = node[ch]
                prefix.append(ch)
            return "".join(prefix) if END in node else word

        return " ".join(replace(w) for w in sentence.split())
