class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]

        for word in strs:
            match_len = min(len(prefix), len(word))
            for i in range(match_len):
                if prefix[i] != word[i]:
                    match_len = i
                    break
            prefix = word[:match_len]

        return prefix