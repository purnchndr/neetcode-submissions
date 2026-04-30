class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        for num in nums:
                map[num] = map.get(num, 0) + 1
        sorted_nums = sorted(map, key=map.get, reverse=True)
        return sorted_nums[:k]

        