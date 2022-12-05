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
>> That too is possible. But in the case where the value of 'n' is 'target / 2', if a second element with the same value does not exist it will
point to the same index (if another element with the same value exists it will overwrite the first value of the index 
in the hash table), and to overcome this we'll have to compare the index of the current element with the index in the 
hash table. 
"""

# Time complexity: O(N)
# Space complexity: O(N)
