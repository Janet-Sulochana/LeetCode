class Solution:
    def reorderSpaces(self, text: str) -> str:
        words=text.split()
        total_spaces=text.count(' ')
        num_words=len(words)
        if num_words==1:
            return words[0]+' '*total_spaces
        gap=total_spaces//(num_words-1)
        extra=total_spaces%(num_words-1)
        return (' '*gap).join(words)+(' '*extra)