class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped_indices = {};
        grouped = [];
        for word in strs:
            freq = [0] * 26;
            for char in word:
                freq[ord(char) - ord('a')] += 1;
            
            if str(freq) not in grouped_indices:
                grouped_indices[str(freq)] = len(grouped);
                grouped.append([word]);
            else:
                word_group = grouped[grouped_indices[str(freq)]]
                word_group.append(word);
            
        return grouped;


