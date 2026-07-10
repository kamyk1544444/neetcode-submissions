class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        a,b= nums1, nums2

        if len(b) < len(a):
            a,b = b,a

        total = len(a) + len(b)

        half = total // 2

        l,r = 0,len(a)-1

        while True:

            i = l+(r-l)//2
            j= half -i-2

            aleft = a[i] if i>= 0 else float("-infinity")
            aright = a[i+1] if i+1 < len(a) else float("infinity") 
            bleft = b[j] if j>= 0  else float("-infinity")
            bright = b[j+1] if j<len(b)  else float("infinity")

            if aright >= bleft and aleft <= bright:
                if total % 2:
                    return (min(aright,bright))
                return (min(aright,bright) + max(aleft,bleft)) / 2
            elif aleft > bright:
                r = i-1
            else:
                l = i+1