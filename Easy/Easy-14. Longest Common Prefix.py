"""
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
Input: ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Note:
All given inputs are in lowercase letters a-z.

"""
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs)==0:
            return ""
    
        lengths = []   
        for string in strs:
            lengths.append(len(string))
        len_max = max(lengths)
        
        strs_new = []
        for string in strs:
            strs_new.append(string+"A"*(len_max-len(string)))
        
        premix=""
        
        for i in range(len_max):
            flag = True
            first = strs_new[0][i]
            for j in range(len(strs_new)-1):
                if first != strs_new[j+1][i]:
                    flag = False
                    break
            if flag==False:
                break
            else:
                premix +=first
        return premix
 ###beat 97.8%
 
 ######### other solutions ########
 """
 https://leetcode.com/problems/longest-common-prefix/discuss/6911/Simple-Python-solution
 people use zip, enumerate function.
 """
 
class Solution(object):
  def longestCommonPrefix(self, strs):
      result = ""       
      for n in zip(*strs):
          if len(set(n)) == 1:
              result += n[0]
          else:
              return result
      return result
   
class Solution:
# @return a string
  def longestCommonPrefix(self, strs):
      if not strs:
          return ""

      for i, letter_group in enumerate(zip(*strs)):
          if len(set(letter_group)) > 1:
              return strs[0][:i]
      else:
          return min(strs)
          
###############what is zip function

https://www.cnblogs.com/waltsmith/p/8029539.html
https://www.cnblogs.com/wushuaishuai/p/7766470.html

#################what is enumerate function
http://www.runoob.com/python/python-func-enumerate.html
