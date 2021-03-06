'''
首先是两个核心位运算： 1.x & -x。这个操作可以保留最后一位1，而其他位都会清零。
比如，一个8位数，00110110.进行了这个操作后就会变为00000010.我在这里想了很久，也没明白原因，
后来发现原来是之前学的东西都还给了老师。。。这里的关键是：计算机存储数的时候存储的是补码，正数的补码是其本身，
而负数的补码是其反码加1.因此，00110110加一个负号以后就变成了10110110（姑且认为最高位是符号位），
其反码为11001001，补码为11001010。这个跟原来的数按位与后就是00000010，神奇✔ 2.x & (x - 1)。
将最后一位1变为0。可以先这么考虑一下，最低位如果是1，减1后就变为了0，按位与后，其他位不发生变化，
最低位清为0.现在考虑更复杂的情况，如果最低位是0，那么减1后，这个0就变为了1，并且向高位借位，
直到遇到第一个1，这个1会因为之前的借位变成0，此时借位清0，更高位的数据就不会发生变化。这样按位与后，
最低位的1就变成了0，而其他的数并没有变化。这个不难验证，自己举个例子就好了。
'''
class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        
        def dfs(n, row, col, ld, rd):
            if row >= n: 
                res += 1
                return
            bits = ~(col | ld | rd) & ((1 << n) - 1)
            while(bits):
                pick = bits & -bits
                dfs(n, row + 1, col | pick, (ld | pick) << 1 , (rd | pick) >> 1)
                bits &= bits - 1
        
        
        # rs = [0,1,0,0,2,10,4,40,92,352,724,2680]
        dfs(n, 0, 0, 0)
        return res

