class WordDictionary:

    def __init__(self):
        self.children = {}
        self.terminating = False

    def addWord(self, word: str) -> None:
        if len(word) == 0:
            self.terminating = True
            return

        c = word[0]
        if c not in self.children:
            self.children[c] = WordDictionary()
        self.children[c].addWord(word[1:])

    def search(self, word: str) -> bool:
        if len(word) == 0:
            return self.terminating
        
        c = word[0]
        res = False

        if c == ".":
            for dot in self.children:
                res = res or self.children[dot].search(word[1:])
        elif c in self.children:
            res = self.children[c].search(word[1:])
        
        return res
        
