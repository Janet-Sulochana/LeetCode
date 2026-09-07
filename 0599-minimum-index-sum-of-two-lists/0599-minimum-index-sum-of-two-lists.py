class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        res=[]
        mini=float('inf')
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i]==list2[j]:
                    n=i+j
                    if n<mini:
                        mini=n
                        res=[list1[i]]
                    elif n==mini:
                        res.append(list1[i])
        return res
