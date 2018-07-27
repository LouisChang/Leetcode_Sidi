class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        
        # first step is to return empty spaces
        str = str.lstrip()
        
        if len(str) == 0:
            return 0
        
        def helper(s):
            #print s
            start  = 0
            while s[start].isdigit():
                #print start
                start += 1
                if start == len(s):
                    break
            return start
        # check first character to see whether it is valid
        if str[0].isdigit() or str[0] == '-' or str[0] == '+':
            
            if str[0] == '+':
                if len(str[1:]) == 0:
                    return 0
                if not str[1].isdigit():
                    return 0
                number  = int(str[1:helper(str[1:])+1])
            elif str[0] == '-':
                if len(str[1:]) == 0:
                    return 0
                if not str[1].isdigit():
                    return 0
                number = -1* int(str[1:helper(str[1:])+1])
            else:
                number  = int(str[:helper(str)])
                
            # check the range
            if number > pow(2,31) - 1:
                return pow(2,31) - 1

            if number < -1 * pow(2,31):
                return -pow(2,31)

            return number
        else:
            return 0
