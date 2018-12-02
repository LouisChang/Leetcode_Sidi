class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        """
        : method without any packages
        """
        final_res = []
        # String manipulation
        for email in emails:
            i, flag, res = 0, 0, []
            while i < len(email):
                if email[i] == '+':
                    i += 1
                    while i < len(email):
                        if email[i] == '@':
                            res.append('@')
                            break
                        else:
                            i += 1
                    final_res.append(''.join(res) + email[i+1:])
                    flag = 1
                    break
                
                if email[i] == '.':
                    i += 1
                    continue
                    
                res.append(email[i])
                i += 1
                # print res, i
            # print "res is", res
            if flag == 0:
                final_res.append(res.join(''))
                
        return len(set(final_res))

	"""
        : method with Python internal package
        """
        res = set()
        for email in emails:
            localname, domain = email.split('@')
            localname = localname.replace('.', '')
            if '+' in localname:
                localname = localname[:localname.index('+')]
            # print localname
            res.add(localname + '@' + domain)
