class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        cha_in = {'(':1,'{':2,'[':3}
        cha_out = {')':1,'}':2,']':3}
        stack = []
        for i in range(len(s)):
            if s[i] in cha_in:
                stack.append(s[i])
            else:
                if stack == []:
                    return False
                else:
                    out = stack.pop()
                    if cha_in[out] != cha_out[s[i]]:
                        return False
        
        if stack != []:
            return False
        return True
