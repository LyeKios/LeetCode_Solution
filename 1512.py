def numIdenticalPairs(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        for index, val in enumerate(nums):
            print(index)
            for ind, item in enumerate(nums):
                if item == val and ind > index:
                    i += 1
        return i
    
if __name__ == "__main__":
    print(numIdenticalPairs([1,2,3,1,1,3]))