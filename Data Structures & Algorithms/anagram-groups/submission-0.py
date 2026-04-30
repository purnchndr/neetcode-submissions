class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for item in strs:
            key = "".join(sorted( item ))
            if key not in anagrams:
                anagrams[key]= []
            anagrams[key].append(item)
        result = []
        return list(anagrams.values())

            
        