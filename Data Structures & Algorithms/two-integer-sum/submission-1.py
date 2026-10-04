class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}

        for i, num in enumerate(nums):
            req = target - num
            if req not in dict:
                dict[num] = i
            else:
                return [dict[req], i]
        