class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a_int = int(a,2)
        b_int = int(b,2)
        output = a_int + b_int
        return str(bin(output)[2:])
