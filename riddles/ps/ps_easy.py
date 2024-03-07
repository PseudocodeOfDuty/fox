from collections import defaultdict
import heapq


class Easy:
    def topRecurrences(self, words: list[str], x: int) -> list[str]:
        count = defaultdict(lambda: [0, ""])

        # negative frequency for heaping
        for word in words:
            count[word] = [count[word][0] - 1, word]

        # list of [frequencies, words]
        lst = list(count.values())

        # heaping
        heapq.heapify(lst)

        # get smallest from the min heap (smallest negative = most frequent)
        lst = heapq.nsmallest(x, lst)

        ans = [ele[1] for ele in lst]
        return ans
