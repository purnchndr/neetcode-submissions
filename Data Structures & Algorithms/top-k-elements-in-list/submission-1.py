class Solution:
    def topKFrequent1(self, nums: List[int], k: int) -> List[int]:
        map = {}
        for num in nums:
                map[num] = map.get(num, 0) + 1
        sorted_nums = sorted(map, key=map.get, reverse=True)
        return sorted_nums[:k]

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        fre = {}
        for num in nums:
            fre[num] =  fre.get(num, 0) + 1
        count = [ [] for i in range(len(nums)+1) ]

        for n, c in fre.items():
            count[c].append(n)
        res = []
        for i in range(len(count)-1, 0, -1):
            for n in count[i]:
                res.append(n)
                if len(res) == k:
                    return res