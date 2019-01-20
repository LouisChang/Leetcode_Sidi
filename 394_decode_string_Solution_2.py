class Solution(object):
    
    def decodeString(self, s):
        return self.decodeStringInternal(s, 1)
        
    def decodeStringInternal(self, s, repeat):
        num = ""
        parenCnt = 0
        strToRepeat = ""
        res = ""
        for c in s:
            if parenCnt == 0:
                if c.isdigit():
                    num += c
                if c == '[':
                    parenCnt += 1
                if (c >= 'a' and c <= 'z') or (c >= 'A' and c <= 'Z'):
                    res += c
            elif c == '[':
                parenCnt += 1
                strToRepeat += c
            elif c == ']':
                parenCnt -= 1
                if parenCnt == 0:
                    res += self.decodeStringInternal(strToRepeat, int(num))
                    strToRepeat,num = "", ""
                else:
                    strToRepeat += c
            else:
                strToRepeat += c
        return res * repeat
    """
    def decodeString(self,s):
        i = 0
        res, i =  self.decodeStringInternal(s,i)
        print("final", res, i)
        return res
    
    def decodeStringInternal(self, s, i):
        print("Hello", i)
        res = ""
        while i < len(s) and s[i] != ']':
            if not s[i].isdigit():
                res += s[i]
                i += 1
            else:
                num = ""
                while s[i].isdigit():
                    num += s[i]
                    i += 1
                i += 1 # skip '['
                tmp, i = self.decodeStringInternal(s, i)
                print("Hi", tmp, num)
                res += tmp * int(num)
                i += 1 # skip ']'
                
        return res, i
        """
