class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        d={"type":0,"color":1,"name":2}
        return sum(item[d[ruleKey]]==ruleValue for item in items)