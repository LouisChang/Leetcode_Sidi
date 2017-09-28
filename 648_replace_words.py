class Solution(object):
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        # create a dictionary to store the root key, pair for search purposes
        real_dic = {}
        length_list = []
        for item in dict:
            real_dic[item] = 1
            length_list.append(len(item))
        # split the sentence into word list
        length_list = sorted(list(set(length_list)))
        
        split_sen = sentence.split()
        res = []
        for word in split_sen:
            flag = 0
            for l in length_list:
                # if root exists, replace the word with shortest root
                if l < len(word) and word[:l] in real_dic:
                    res.append(word[:l])
                    flag = 1
                    break
            if flag == 0:   
                res.append(word)
        return ' '.join(res)
