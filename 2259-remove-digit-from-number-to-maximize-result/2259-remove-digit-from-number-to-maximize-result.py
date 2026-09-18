class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        l=-1
        for i in range(len(number)):
            if number[i]==digit:
                if i+1<len(number) and number[i+1]>digit:
                    return number[:i]+number[i+1:]
                l=i
        return number[:l]+number[l+1:]