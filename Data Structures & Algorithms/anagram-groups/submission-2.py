class Solution:
    def groupAnagrams2(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for item in strs:
            key = "".join(sorted( item ))
            if key not in anagrams:
                anagrams[key]= []
            anagrams[key].append(item)
        result = []
        for lists in anagrams.values():
            result.append(lists)
        return result

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana = {}

        for st in strs:
            fre = [0] * 26

            for c in st:
                fre[ord(c) - ord('a')] += 1
            key = tuple(fre)

            if key not in ana:
                ana[key] = []
            ana[key].append(st)
        return list( ana.values())

            
        