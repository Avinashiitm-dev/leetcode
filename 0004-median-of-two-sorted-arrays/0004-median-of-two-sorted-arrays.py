class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        newl=sorted(nums1+nums2)
        if len(newl)%2!=0:
            return float(newl[len(newl)//2])
        else:
            a=newl[(len(newl)//2)-1]
            b=newl[len(newl)//2]
            return float((a+b)/2)

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna