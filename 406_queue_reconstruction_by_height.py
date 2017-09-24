class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        # store people based on their height(h)
        peopledic = {}
        # store all the key
        key = []
        res = []
        for ppl in people:
            if ppl[0] in peopledic:
                peopledic[ppl[0]].append(ppl)
            else:
                peopledic[ppl[0]] = [ppl]
                key.append(ppl[0])
        key.sort(reverse = True)
        for k in key:
            new = sorted(peopledic[k],key = lambda x:x[1])
            for item in new:
                res.insert(item[1],item)

        return res
