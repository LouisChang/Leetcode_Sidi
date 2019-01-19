class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        num = ""
        res = ""
        bucket_count = 0
        start_index, curr_index, end_index = 0, 0, len(s)-1

        for ch in s:
            if ch.isdigit() and bucket_count == 0:
                num += ch
            elif ch == '[':
                if bucket_count == 0:
                    start_index = curr_index
                bucket_count += 1
            elif ch == ']':
                bucket_count -= 1
                if bucket_count == 0:
                    end_index = curr_index

                if bucket_count == 0:
                    #print(num, type(num), start_index, end_index, curr_index)
                    res += int(num)*self.decodeString(s[start_index + 1: end_index])
                    #print(res)
                    num = ""

            else:
                if bucket_count == 0:
                    res += ch
            curr_index += 1

        return res
