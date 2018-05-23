# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: 
# (you may want to display this pattern in a fixed font for better legibility)
# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"
# Write the code that will take a string and make this conversion given a number of rows:
# string convert(string s, int numRows);

## Example 1:
## Input: s = "PAYPALISHIRING", numRows = 3
## Output: "PAHNAPLSIIGYIR"

##note the special case when numRows =2

class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        
        if numRows == 1:
            return s      
        elif numRows == 2:
            line1 = []
            line2 = []
            for c in range(len(s)):
                if c%2 ==0:
                    line1.append(s[c])
                else:
                    line2.append(s[c])
            return "".join(line1+line2)
        else:  
            div = 2*numRows-2

            line ={}
            for item in range(numRows):
                line[item]=[]

            for i in range(len(s)):
                if i%div >= numRows:
                    index = div-i%div
                else:
                    index = i%div
                line[index].append(s[i])

            newS=[]
            for items in line.items():
                newS+=items[1]
            return "".join(newS)
 ######### beat 58%
 
 ##### solution in discussion
 
 ### credit to pharrellyhy
 
 ## https://leetcode.com/problems/zigzag-conversion/discuss/3404/Python-O(n)-Solution-in-96ms-(99.43)
 
 class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s

        L = [''] * numRows
        index, step = 0, 1

        for x in s:
            L[index] += x
            if index == 0:
                step = 1
            elif index == numRows -1:
                step = -1
            index += step

        return ''.join(L)
# its algorithm is hard to understand
######################
# inspired by this solution, I replaced dict with list to store line

class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        
        if numRows == 1:
            return s      
        elif numRows == 2:
            line1 = []
            line2 = []
            for c in range(len(s)):
                if c%2 ==0:
                    line1.append(s[c])
                else:
                    line2.append(s[c])
            return "".join(line1+line2)
        else:  
            div = 2*numRows-2

            line =['']*numRows
            

            for i in range(len(s)):
                if i%div >= numRows:
                    index = div-i%div
                else:
                    index = i%div
                line[index]+=s[i]
            return "".join(line)
#now beat 89.55%


        
        
 
