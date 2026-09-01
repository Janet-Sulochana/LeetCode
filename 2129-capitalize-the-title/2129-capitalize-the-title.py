class Solution:
    def capitalizeTitle(self, title: str) -> str:
        res=[]
        for i in title.split():
            if len(i)>=3:
                res.append(i.capitalize())
            else:
                res.append(i.lower())
        return " ".join(res)
