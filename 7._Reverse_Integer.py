"""

Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.Assume the environment does not allow you to store 64-bit integers (signed or unsigned). Example 1:Example 2:Example 3:Example 4: Constraints:


""""

"""

Input: x = 123
Output: 321
Input: x = -123
Output: -321
Input: x = 120
Output: 21
Input: x = 0
Output: 0



""""

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
​
