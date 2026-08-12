class Solution:
    def jump(self, nums: List[int]) -> int:
        
        poczatek = skok_koncowy = 0

        najdalej = 0
        wynik = 0
        while skok_koncowy < len(nums)-1:

            for j in range(poczatek,skok_koncowy+1):
                najdalej = max(najdalej,j+nums[j])
            
            poczatek = skok_koncowy+1
            skok_koncowy = najdalej
            wynik +=1

        return wynik