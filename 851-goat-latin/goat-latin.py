
class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowels = set("aeiouAEIOU")
        res = []
        for i, w in enumerate(sentence.split(), 1):
            if w[0] in vowels:
                res.append(w + "ma" + "a" * i)
            else:
                res.append(w[1:] + w[0] + "ma" + "a" * i)
        return " ".join(res)
