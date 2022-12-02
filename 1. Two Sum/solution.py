class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_elems = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prev_elems:
                return [prev_elems[diff], i]
            prev_elems[n] = i


"""
Why not first create the hash table/map first and then search?
>> It will consider the same element twice if the value of `n` is `target / 2`. To solve that we will need to check the 
indices of the values.  
"""

# Time complexity: O(n)
# Space complexity: O(n)
