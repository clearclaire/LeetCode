class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = str(x)
        back_num = ''
        for i in range(1, len(num)+1):
            back_num += num[-i]
            
        if num == back_num :
            return True
            