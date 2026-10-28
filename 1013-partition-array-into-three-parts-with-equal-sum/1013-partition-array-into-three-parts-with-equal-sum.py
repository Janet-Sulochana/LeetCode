class Solution:
    def canThreePartsEqualSum(self, arr: list[int]) -> bool:
        t_s=sum(arr)
        if t_s%3!=0:
            return False
        target=t_s//3
        curr_sum=0
        parts_found=0
        for i in range(len(arr)-1):
            curr_sum+=arr[i]
            if curr_sum==target:
                parts_found+=1
                curr_sum=0
                if parts_found==2:
                    return True
        return False