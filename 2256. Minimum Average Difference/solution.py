class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)
        min_avg_diff = math.inf
        min_avg_diff_idx = -1
        total = sum(nums)

        curr_prefix_sum = 0
        for i in range(n):
            curr_prefix_sum += nums[i]
            curr_suffix_sum = total - curr_prefix_sum
            curr_avg_diff = (curr_prefix_sum // (i + 1)) - ((curr_suffix_sum // (n - i - 1)) if n - i - 1 else 0)
            if (abs_diff := abs(curr_avg_diff)) < min_avg_diff:
                min_avg_diff = abs_diff
                min_avg_diff_idx = i
        return min_avg_diff_idx

# Time complexity: O(N)
# Space complexity: O(1)
