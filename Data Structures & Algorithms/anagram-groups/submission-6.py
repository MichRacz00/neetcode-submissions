class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for word in strs:
            sorted_word = str(sorted(word))
            anagrams = res.get(sorted_word, [])
            anagrams.append(word)
            res[sorted_word] = anagrams
        
        return list(res.values())