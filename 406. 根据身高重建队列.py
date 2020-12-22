"""
假设有打乱顺序的一群人站成一个队列。 每个人由一个整数对(h, k)表示，其中h是这个人的身高，k是排在这个人前面且身高大于或等于h的人数。 编写一个算法来重建这个队列。

注意：
总人数少于1100人。

示例

输入:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

输出:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
"""
class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]

        先对输入数组排序，h升序，k降序 从头循环遍历 当前这个人就是剩下未安排的人中最矮的人，他的k值就代表他在剩余空位的索引值 如果有多个人高度相同，要按照k值从大到小领取索引值 示例：

[ 0, 1, 2, 3, 4, 5 ] [ 4, 4 ] 4
[ 0, 1, 2, 3, 5 ]    [ 5, 2 ] 2
[ 0, 1, 3, 5 ]       [ 5, 0 ] 0
[ 1, 3, 5 ]          [ 6, 1 ] 3
[ 1, 5 ]             [ 7, 1 ] 5
[ 1 ]                [ 7, 0 ] 1
[ [ 5, 0 ], [ 7, 0 ], [ 5, 2 ], [ 6, 1 ], [ 4, 4 ], [ 7, 1 ] ]
        """
        people = sorted(people, key = (lambda x:(x[0],-x[1])))
        # print people
        left, right = 0, 1
        # while right < len(people):
        #     if people[left][0] == people[right][0]:
        #         right += 1
        #         people[left:right] = sorted(people[left:right], reverse = True)
        #     else:
        #         left = right
        #         right += 1
        index = [i for i in range(len(people))]
        res = [0 for _ in range(len(people))]
        # print res

        for p in people:
            ind = index[p[1]]
            res[ind] = p
            index.remove(ind)
        return res
    
class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        '''
            首先要记得一点，高的人不会受低的人影响，所以优先处理高的人，排序完后，
            按从高到低和优先级处理，先处理高的并且序号小的，序号便是插入的位置
        '''

        # 身高从高到底排，位置从低往高排
        people = sorted(people, key=lambda x:(-x[0],x[1]))
        res = []
        for i in people:
            res.insert(i[1],i)
        return res

