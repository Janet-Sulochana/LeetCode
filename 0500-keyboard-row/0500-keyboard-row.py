class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows=["qwertyuiop","asdfghjkl","zxcvbnm"]
        return [word for word in words if any(set(word.lower())<=set(row) for row in rows)]