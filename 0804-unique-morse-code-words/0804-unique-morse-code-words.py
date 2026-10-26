class Solution:
    def uniqueMorseRepresentations(self, words: list[str]) -> int:
        morse=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        trans=set()
        for word in words:
            tran="".join(morse[ord(char)-ord('a')] for char in word)
            trans.add(tran)
        return len(trans)