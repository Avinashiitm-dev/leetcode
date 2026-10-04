class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        mapping={')':'(','}':'{',']':'['}
        for i in s:
            if i in mapping:
                top=stack.pop() if stack else '#'
                if mapping[i]!=top:
                    return False
            else:
                stack.append(i)
        return not stack

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna