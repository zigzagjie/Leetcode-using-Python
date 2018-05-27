"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.
Example 1:
Input: "()"
Output: true
Example 2:
Input: "()[]{}"
Output: true
Example 3:
Input: "(]"
Output: false
Example 4:
Input: "([)]"
Output: false
Example 5:
Input: "{[]}"
Output: true
"""
###
# i did not solve this problem myself.i checked the discussion board and found they used STACK structure.
### the main idea is that if you meet the first ),}, or ], it should be followed strictly by its friend.


Therefore, here is the solution.

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
 
    
        list1 = ['[','(','{']
        list2 = [']',')','}']
        
        length = len(s)
        
        if length==0:
            return True
        if length%2 ==1:
            return False
    
        stack = []
        
        for i in range(len(s)):
            if s[i] in list1:
                stack.append(s[i])
            elif s[i] in list2:
                if stack==[] or stack.pop()!= list1[list2.index(s[i])]:
                    return False
        return stack==[]
 ####stack is an important data structure. 
 ### beat 99.85%
 
 #### append/pop in Python
 # https://www.cnblogs.com/pureLaw/archive/2017/01/16/6291323.html
 # https://blog.csdn.net/dongrixinyu/article/details/78775057
 
 ### other smart solutions but takes longer time
 # https://leetcode.com/problems/valid-parentheses/discuss/9225/Python-is-this-a-cheating-method-accepted-with-40ms-easy-to-understand-but
 class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        if n == 0:
            return True
        
        if n % 2 != 0:
            return False
            
        while '()' in s or '{}' in s or '[]' in s:
            s = s.replace('{}','').replace('()','').replace('[]','')
        
        if s == '':
            return True
        else:
            return False
            
            
            

