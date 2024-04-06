# from collections import defaultdict


# class Solution:
#     def customSortString(self, order: str, s: str) -> str:
#         sort_key = defaultdict(int)

#         for i, ch in enumerate(order, start=1):
#             # Because the default value for characters not in 'order' string is going to be 0,
#             # hence we start the ones in it with 1.
#             sort_key[ch] = i

#         return "".join(sorted(s, key=sort_key.__getitem__))


from collections import Counter


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        counter = Counter(s)
        result = []

        for ch in order:
            if ch in counter:
                result.append(ch * counter[ch])
                del counter[ch]

        result.extend(ch * count for ch, count in counter.items())

        return "".join(result)
