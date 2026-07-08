class Solution:
    def findMin(self, nums: List[int]) -> int:
        

        l,r = 0,len(nums)-1

        wynik = 100000

        while r>= l:

            mid = l + (r-l) // 2

            wynik = min(wynik,nums[mid])

            if nums[r] > nums[l]:
                r = mid -1
            else:
                if nums[mid] < nums[l]:
                    r = mid-1
                else:
                    l = mid+1
        return wynik
