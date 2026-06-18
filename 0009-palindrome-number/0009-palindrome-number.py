class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x < 0:
            return False
        
        t = x
        res = 0
        while t > 0:
            r = t % 10
            res = res * 10 + r
            t = t // 10
            
        return res == x   