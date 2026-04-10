class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        if len(digits) == 0:
            return []

        q = [""]
        for digit in digits:
            newQ = []
            for curLetters in q:
                for c in digitToChar[digit]:
                    curLetters += c
                    newQ.append(curLetters)
                    curLetters = curLetters[:-1]
            q = newQ
        
        return q