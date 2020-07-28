class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        
        for ch in tokens:
            if ch not in ['+', '-', '*', '/']:
                stack.append(int(ch))
            else:
                second = stack.pop()
                first = stack.pop()
                if ch == '+':
                    stack.append(first+second)
                elif ch == '-':
                    stack.append(first-second)
                elif ch == '*':
                    stack.append(first*second)
                else:
                    if first/second < 0 and first % second != 0:
                        stack.append(first/second+1)
                    else:
                        stack.append(first/second)
        return stack[0]
