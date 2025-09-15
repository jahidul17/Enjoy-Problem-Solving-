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
target = 18
print(Solution().twoSum(nums, target))  # Output: [0, 1]

#another way

# store={}
# for j, x in enumerate(nums):
#     complement=target-x
#     if complement in store:
#         print([store[complement],j])
#     store[x]=j
    # print(store)
