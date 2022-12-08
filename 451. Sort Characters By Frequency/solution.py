class Solution:
    def frequencySort(self, s: str) -> str:
        return "".join(ch * freq for ch, freq in Counter(s).most_common())

# Time complexity: O(NLogN)
# Space complexity: O(N)

class Solution:
    def frequencySort(self, s: str) -> str:
        counter = {}
        for ch in s:
            counter[ch] = counter.get(ch, 0) + 1
        
        
