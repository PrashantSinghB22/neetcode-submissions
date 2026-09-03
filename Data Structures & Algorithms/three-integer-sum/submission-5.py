class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        result = []

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            target = -nums[i]

            while left < right:
                current = nums[left] + nums[right]

                if current < target:
                    left += 1
                elif current > target:
                    right -= 1
                else:
                    result.append([
                        nums[i], 
                        nums[left], 
                        nums[right]
                        ])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
        return result






        