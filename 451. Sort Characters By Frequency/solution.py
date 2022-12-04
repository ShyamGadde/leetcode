class Solution:
    def frequencySort(self, s: str) -> str:
        return "".join(ch * freq for ch, freq in Counter(s).most_common())

# Time complexity: O(NlogN)
# Space complexity: O(N)
