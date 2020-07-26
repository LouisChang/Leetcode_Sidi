class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        # initiliaze a stack, num and operator
        s += '+0'
        stack = []
        num = 0
        operator = "+"
        
        for ch in s:
            if ch == ' ':
                pass
            elif ch.isdigit():
                num = num*10 + int(ch)
            else:
                if operator == '+':
                    stack.append(num)
                elif operator == '-':
                    stack.append(-num)
                elif operator == '*':
                    stack.append(stack.pop()*num)
                else:
                    curr = stack.pop()
                    if curr % num != 0 and curr < 0:
                        stack.append(curr/num+1)
                    else:
                        stack.append(curr/num)
                
                operator = ch
                num = 0
            
                
        return sum(stack)
