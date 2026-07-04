class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        max_nums = 0
        amount_flipped = 0

        for i in range(len(nums)):
            if (nums[i] == 0):
                amount_flipped += 1
            
            if amount_flipped > k:
                while (amount_flipped > k):
                    if (nums[left] == 1):
                        left+= 1
                    elif (nums[left] == 0):
                        amount_flipped -= 1
                        left += 1
            current_window = i - left + 1
            max_nums = max(max_nums, current_window)
        return max_nums

        
