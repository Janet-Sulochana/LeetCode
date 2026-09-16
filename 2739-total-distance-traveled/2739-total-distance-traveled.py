class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        d=0
        while mainTank>=5:
            d+=50
            mainTank-=5
            if additionalTank>=1:
                additionalTank-=1
                mainTank+=1
        d+=mainTank*10
        return d