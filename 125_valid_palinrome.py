class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        head = 0
        s = s.lower()
        s = s.strip()
        #print s
        tail = len(s) -1
        while head < tail:
            while not s[head].isalnum() and head < len(s)-1 :
                head += 1
            
            while not s[tail].isalnum() and tail > 0:
                tail -= 1
            
            if head >= tail:
                break
            if s[head] != s[tail]:
                return False
            
            head += 1
            tail -= 1
        
        return True
