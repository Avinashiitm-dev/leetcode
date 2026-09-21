class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        sett=set()
        longest=0
        for i in range(len(s)):
            while s[i] in sett:
                sett.remove(s[l])
                l+=1
            w=(i-l)+1
            longest=max(longest,w)
            sett.add(s[i])
        return longest


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna