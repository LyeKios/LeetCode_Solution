list = \
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

word = 'F'

def Traversal(list, target):
    '''
    list: board
    target: the alphabet to traversal
    return: the index of target
    '''
    tar = []
    for index, item in enumerate(list):
        for index_1, item_1 in enumerate(item):
            if target == item_1:
                tar.append([index, index_1])
    return tar

def search(list, index, target, direction):
    '''
    list: board
    index: current address
    target: the next alphabet to search
    direction: the direction of the front alphabet, means[east, south, west, north]
    return: bool, direction
    '''
    Max_y, Max_x = len(list), len(list[0])
    x, y = index
    bool = 0
    
    if index ==[0, 0]:
        if direction[2]:
            if list[x][y+1] == target:
                bool = bool + (list[x][y+1] == target)
                direction = [0, 0, 0, 1]
        if direction[1]:
            if list[x+1][y] == target:
                bool = bool + (list[x+1][y] == target)
                direction = [1, 0, 0, 0]
        if direction == [0, 0, 0, 0]:
            if list[x+1][y] == target:
                bool = bool + (list[x+1][y] == target)
                direction = [1, 0, 0, 0]
            if list[x][y+1] == target:
                bool = bool + (list[x][y+1] == target)
                direction = [0, 0, 0, 1]

    if index ==[0, Max_y]:
        if direction[2]:
            if list[x][y-1] == target:
                bool = bool + (list[x][y-1] == target)
                direction = [0, 1, 0, 0]
        if direction[3]:
            if list[x+1][y] == target:
                bool = bool + (list[x+1][y] == target)
                direction = [1, 0, 0, 0]
        if direction == [0, 0, 0, 0]:
            if list[x+1][y] == target:
                bool = bool + (list[x+1][y] == target)
                direction = [1, 0, 0, 0]
            if list[x][y-1] == target:
                bool = bool + (list[x][y-1] == target)
                direction = [0, 1, 0, 0]

    if index ==[Max_x, 0]:
        if direction[0]:
            if list[x][y+1] == target:
                bool = bool + (list[x][y+1] == target)
                direction = [0, 0, 0, 1]
        if direction[1]:
            if list[x-1][y] == target:
                bool = bool + (list[x-1][y] == target)
                direction = [0, 0, 1, 0]
        if direction == [0, 0, 0, 0]:
            if list[x][y+1] == target:
                bool = bool + (list[x][y+1] == target)
                direction = [0, 0, 0, 1]
            if list[x-1][y] == target:
                bool = bool + (list[x-1][y] == target)
                direction = [0, 0, 1, 0]

    if index ==[Max_x, Max_y]:
        if direction[0]:
            if list[x][y-1] == target:
                bool = bool + (list[x][y-1] == target)
                direction = [0, 1, 0, 0]
        if direction[3]:
            if list[x-1][y] == target:
                bool = bool + (list[x-1][y] == target)
                direction = [0, 0, 1, 0]
        if direction == [0, 0, 0, 0]:
            if list[x][y-1] == target:
                bool = bool + (list[x][y-1] == target)
                direction = [0, 1, 0, 0]
            if list[x-1][y] == target:
                bool = bool + (list[x-1][y] == target)
                direction = [0, 0, 1, 0]
                

    if x == 0 and y != 0 and y != Max_y:
        if direction[1]:
            if list[x+1][y] == target:
                bool = bool + (list[x+1][y] == target)
                direction = [1, 0, 0, 0]
            if list[x][y-1] == target:
                bool = bool + (list[x][y-1] == target)
                direction = [0, 1, 0, 0]
        if direction[2]:
            if list[x][y-1] == target:
                bool = bool + (list[x][y-1] == target)
                direction = [0, 1, 0, 0]
            if list[x][y+1] == target:
                bool = bool + (list[x][y+1] == target)
                direction = [0, 0, 0, 1]
        if direction[3]:
            if list[x][y+1] == target:
                bool = bool + (list[x][y+1] == target)
                direction = [0, 0, 0, 1]
            if list[x+1][y] == target:
                bool = bool + (list[x+1][y] == target)
                direction = [1, 0, 0, 0]
        if direction == [0, 0, 0, 0]:
            if list[x+1][y] == target:
                bool = bool + (list[x+1][y] == target)
                direction = [1, 0, 0, 0]
            if list[x][y+1] == target:
                bool = bool + (list[x][y+1] == target)
                direction = [0, 0, 0, 1]
            if list[x][y-1] == target:
                bool = bool + (list[x][y-1] == target)
                direction = [0, 1, 0, 0]

    if y == 0 and x != 0 and x != Max_x:
        if direction[0]:
            if list[x+1][y] == target:
                bool = bool + (list[x+1][y] == target)
                direction = [1, 0, 0, 0]
            if list[x][y+1] == target:
                bool = bool + (list[x][y+1] == target)
                direction = [0, 0, 0, 1]
        if direction[1]:
            if list[x+1][y] == target:
                bool = bool + (list[x+1][y] == target)
                direction = [1, 0, 0, 0]
            if list[x-1][y] == target:
                bool = bool + (list[x-1][y] == target)
                direction = [0, 0, 1, 0]
        if direction[2]:
            if list[x-1][y] == target:
                bool = bool + (list[x-1][y] == target)
                direction = [0, 0, 1, 0]
            if list[x][y+1] == target:
                bool = bool + (list[x][y+1] == target)
                direction = [0, 0, 0, 1]
        if direction == [0, 0, 0, 0]:
            if list[x+1][y] == target:
                bool = bool + (list[x+1][y] == target)
                direction = [1, 0, 0, 0]
            if list[x-1][y] == target:
                bool = bool + (list[x-1][y] == target)
                direction = [0, 0, 1, 0]
            if list[x][y+1] == target:
                bool = bool + (list[x][y+1] == target)
                direction = [0, 0, 0, 1]

    if y == Max_y and x != 0 and x != Max_x:
        if direction[0]:
            if list[x+1][y] == target:
                bool = bool + (list[x+1][y] == target)
                direction = [1, 0, 0, 0]
            if list[x][y-1] == target:
                bool = bool + (list[x][y-1] == target)
                direction = [0, 1, 0, 0]
        if direction[2]:
            if list[x-1][y] == target:
                bool = bool + (list[x-1][y] == target)
                direction = [0, 0, 1, 0]
            if list[x][y-1] == target:
                bool = bool + (list[x][y-1] == target)
                direction = [0, 1, 0, 0]
        if direction[3]:
            if list[x+1][y] == target:
                bool = bool + (list[x+1][y] == target)
                direction = [1, 0, 0, 0]
            if list[x-1][y] == target:
                bool = bool + (list[x-1][y] == target)
                direction = [0, 0, 1, 0]
        if direction == [0, 0, 0, 0]:
            if list[x+1][y] == target:
                bool = bool + (list[x+1][y] == target)
                direction = [1, 0, 0, 0]
            if list[x-1][y] == target:
                bool = bool + (list[x-1][y] == target)
                direction = [0, 0, 1, 0]
            if list[x][y-1] == target:
                bool = bool + (list[x][y-1] == target)
                direction = [0, 1, 0, 0]

    if x == Max_x and y != 0 and y != Max_y:
        if direction[0]:
            if list[x][y+1] == target:
                bool = bool + (list[x][y+1] == target)
                direction = [0, 0, 0, 1]
            if list[x][y-1] == target:
                bool = bool + (list[x][y-1] == target)
                direction = [0, 1, 0, 0]
        if direction[1]:
            if list[x-1][y] == target:
                bool = bool + (list[x-1][y] == target)
                direction = [0, 0, 1, 0]
            if list[x][y-1] == target:
                bool = bool + (list[x][y-1] == target)
                direction = [0, 1, 0, 0]
        if direction[3]:
            if list[x-1][y] == target:
                bool = bool + (list[x-1][y] == target)
                direction = [0, 0, 1, 0]
            if list[x][y+1] == target:
                bool = bool + (list[x][y+1] == target)
                direction = [0, 0, 0, 1]
        if direction == [0, 0, 0, 0]:
            if list[x][y+1] == target:
                bool = bool + (list[x][y+1] == target)
                direction = [0, 0, 0, 1]
            if list[x][y-1] == target:
                bool = bool + (list[x][y-1] == target)
                direction = [0, 1, 0, 0]
            if list[x-1][y] == target:
                bool = bool + (list[x-1][y] == target)
                direction = [0, 0, 1, 0]
    else:
        if direction[0]:
            if list[x+1][y] == target:
                bool = bool + (list[x+1][y] == target)
                direction = [1, 0, 0, 0]
            if list[x][y+1] == target:
                bool = bool + (list[x][y+1] == target)
                direction = [0, 0, 0, 1]
            if list[x][y-1] == target:
                bool = bool + (list[x][y-1] == target)
                direction = [0, 1, 0, 0]
        if direction[1]:
            if list[x+1][y] == target:
                bool = bool + (list[x+1][y] == target)
                direction = [1, 0, 0, 0]
            if list[x-1][y] == target:
                bool = bool + (list[x-1][y] == target)
                direction = [0, 0, 1, 0]
            if list[x][y-1] == target:
                bool = bool + (list[x][y-1] == target)
                direction = [0, 1, 0, 0]
        if direction[2]:
            if list[x-1][y] == target:
                bool = bool + (list[x-1][y] == target)
                direction = [0, 0, 1, 0]
            if list[x][y+1] == target:
                bool = bool + (list[x][y+1] == target)
                direction = [0, 0, 0, 1]
            if list[x][y-1] == target:
                bool = bool + (list[x][y-1] == target)
                direction = [0, 1, 0, 0]
        if direction[3]:
            if list[x+1][y] == target:
                bool = bool + (list[x+1][y] == target)
                direction = [1, 0, 0, 0]
            if list[x-1][y] == target:
                bool = bool + (list[x-1][y] == target)
                direction = [0, 0, 1, 0]
            if list[x][y+1] == target:
                bool = bool + (list[x][y+1] == target)
                direction = [0, 0, 0, 1]
        if direction == [0, 0, 0, 0]:
            if list[x+1][y] == target:
                bool = bool + (list[x+1][y] == target)
                direction = [1, 0, 0, 0]
            if list[x-1][y] == target:
                bool = bool + (list[x-1][y] == target)
                direction = [0, 0, 1, 0]
            if list[x][y+1] == target:
                bool = bool + (list[x][y+1] == target)
                direction = [0, 0, 0, 1]
            if list[x][y-1] == target:
                bool = bool + (list[x][y-1] == target)
                direction = [0, 1, 0, 0]
    # print(bool)
    return bool, direction

from typing import List


class Solution:
    #         (x-1,y)
    # (x,y-1) (x,y) (x,y+1)
    #         (x+1,y)

    directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]

    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        if m == 0:
            return False
        n = len(board[0])

        marked = [[False for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                # 对每一个格子都从头开始搜索
                if self.__search_word(board, word, 0, i, j, marked, m, n):
                    return True
        return False

    def __search_word(self, board, word, index,
                      start_x, start_y, marked, m, n):
        # 先写递归终止条件
        if index == len(word) - 1:
            return board[start_x][start_y] == word[index]

        # 中间匹配了，再继续搜索
        if board[start_x][start_y] == word[index]:
            # 先占住这个位置，搜索不成功的话，要释放掉
            marked[start_x][start_y] = True
            for direction in self.directions:
                new_x = start_x + direction[0]
                new_y = start_y + direction[1]
                # 注意：如果这一次 search word 成功的话，就返回
                if 0 <= new_x < m and 0 <= new_y < n and \
                        not marked[new_x][new_y] and \
                        self.__search_word(board, word,
                                           index + 1,
                                           new_x, new_y,
                                           marked, m, n):
                    return True
            marked[start_x][start_y] = False
        return False

# if __name__ == "__main__":
    '''
    # print(Traversal(list, 'A'))
    tar_index = Traversal(list, word[0])
    for item in tar_index:
        # i = 1
        direction = [0, 0, 0, 0]
        Bool = 1
        for index, val in enumerate(word):
            if Bool:
                Bool, direction = search(list, item, val, direction)
                if Bool and index == (len(word)):
                    print(1)
    '''