class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0, len(nums)-1

        wynik = min(nums[r],nums[l])

        while r>=l:

            if nums[r] > nums[l]:
                wynik = min(wynik, nums[l])
                break

            mid = l + (r-l) // 2
            wynik = min(wynik,nums[mid])
            if nums[l] <= nums[mid]:
                l = mid+1
            else:
                r = mid-1
        
        return wynik

