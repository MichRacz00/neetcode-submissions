class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        s_letters = {};
        t_letters = {};        

        for char in s:
            if char not in s_letters:
                s_letters[char] = 0;
            else:
                s_letters[char] += 1;

        for char in t:
            if char not in t_letters:
                t_letters[char] = 0;
            else:
                t_letters[char] += 1;
    
        return s_letters == t_letters;

        