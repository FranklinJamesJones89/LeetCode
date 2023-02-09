#! python3

def twoSum(nums, target):
    prevMap = {} #val : index
    for index, value in enumerate(nums):
        diff = target - value
        if diff in prevMap:
            print(prevMap[diff], index)
        else:
            prevMap[value] = index

twoSum([2,7,11,15], 9)

