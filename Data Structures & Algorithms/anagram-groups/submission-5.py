class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        classified_words = {}

        for word in strs:
            sorted_word = str(sorted(word))
            words = classified_words.get(sorted_word, [])
            words.append(word)
            classified_words[sorted_word] = words

        return list(classified_words.values())

            
