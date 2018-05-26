# Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
## Example 1:
## Input: 121
## Output: true

## Input: -121
## Output: false
## Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        rtype = True
        if x<0:
            return False
        elif x<10:
            return True
        elif x%10==0:
            return False
        else:
            did = 10
            while x//did >=10:
                did*=10
                
            did2=1
            while did>=did2:
                if (x//did2)%10!=(x//did)%10:
                    rtype=False
                did/=10
                did2*=10
            return rtype
## beat 35%

