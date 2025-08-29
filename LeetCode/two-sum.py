class Solution(object):
    def twoSum(self, nums, target):
        hashmap = {}  # stores number -> index
        for i, num in enumerate(nums):
            complement = target - num
            if complement in hashmap:
                print("Found:", (hashmap[complement], i))
                return [hashmap[complement], i]
            hashmap[num] = i
            print(i)
            
        return []

nums = [2, 7, 11, 15]
target = 26
print(Solution().twoSum(nums, target))  # Output: [0, 1]
