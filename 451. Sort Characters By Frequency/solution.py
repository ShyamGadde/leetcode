class Solution:
    def frequencySort(self, s: str) -> str:
        frequency = Counter(s).most_common()
        return "".join([ele[0] * ele[1] for ele in frequency])