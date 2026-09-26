class Solution:
    def reverse(self, x: int) -> int:
        sttr=str(x)
        if sttr[0]=="-":
            ans="-"+sttr[1:][::-1]
        else:
            ans=sttr[::-1]
        rev=int(ans)
        if rev < -2**31 or rev > 2**31 - 1:
            return 0
        return rev

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna