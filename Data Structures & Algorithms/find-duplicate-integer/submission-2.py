class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        szybko, wolno = 0,0

        while True:
            szybko = nums[nums[szybko]]
            wolno = nums[wolno]
            if wolno == szybko:
                break
        
        wolno2=0

        while True:

            wolno=nums[wolno]
            wolno2=nums[wolno2]

            if wolno2 == wolno:
                return wolno