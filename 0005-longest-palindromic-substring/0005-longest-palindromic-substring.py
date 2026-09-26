class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s :
            return ''
        
        ans=''
        for i in range(len(s)):
            odd_pallindrome=self.expand(s,i,i)
            even_pallindrome=self.expand(s,i,i+1)
            if len(odd_pallindrome)>len(ans):
                ans=odd_pallindrome
            if len(even_pallindrome)>len(ans):
                ans=even_pallindrome
        return ans
    def expand(self,s:str,left:int,right:int):
            while left>=0 and right<len(s) and s[left]==s[right]:
                left-=1
                right+=1
            return s[left+1:right]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna