class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        covered = [False] * (right - left + 1)

        for start, end in ranges:
            for x in range(max(start, left), min(end, right) + 1):
                covered[x - left] = True

        return all(covered)

# Time Complexity: O(n * (right - left + 1))
# Space Complexity: O(right - left + 1)