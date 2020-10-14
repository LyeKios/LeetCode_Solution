'''
给定仅有小写字母组成的字符串数组 A，返回列表中的每个字符串中都显示的全部字符（包括重复字符）组成的列表。例如，如果一个字符在每个字符串中出现 3 次，但不是 4 次，则需要在最终答案中包含该字符 3 次。

你可以按任意顺序返回答案。

输入：["bella","label","roller"]
输出：["e","l","l"]
'''
from collections import Counter
class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        '''
        def getCharList(Item):
            retype = [[], []]
            Item.sort()
            for alphbet in Item:
                if alphbet not in retype[0]:
                    retype[0].append(alphbet)
                    retype[1].append(1)
                    continue
                retype[1][retype[0].index(alphbet)] += 1
            return retype
                
        countList = []
        for item in A:
            countList.append(getCharList(item))
        '''
        ans = []
        anString = Counter(A[0])
        for i in range(len(A) - 1):
            anString = (anString & Counter(A[i + 1])) 
            # print(anString)
        for i in anString:
            if anString['{}'.format(i)] == 1:
                ans.append(i)
                continue
            for j in range(anString['{}'.format(i)]):
                ans.append(i)
        return ans