class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        szybko,wolno = 0,0

        while True:
            szybko = nums[nums[szybko]]
            wolno = nums[wolno]

            if szybko == wolno:
                break
            

        wolno2 = 0

        while True:
            wolno2 = nums[wolno2]
            wolno = nums[wolno]
            if wolno == wolno2:
                return wolno

            
