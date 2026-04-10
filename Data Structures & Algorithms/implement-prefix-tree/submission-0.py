class PrefixTree:

    def __init__(self):
        self.children = {}
        self.terminating = False

    def insert(self, word: str) -> None:
        if len(word) == 0:
            self.terminating = True
            return

        c = word[0]
        if c not in self.children:
            self.children[c] = PrefixTree()
        return self.children[c].insert(word[1:])      

    def search(self, word: str) -> bool:
        if len(word) == 0:
            return self.terminating
        
        c = word[0]
        if c in self.children:
            return self.children[c].search(word[1:])
        
        return False
        

    def startsWith(self, prefix: str) -> bool:
        if len(prefix) == 0:
            return True

        c = prefix[0]
        if c in self.children:
            return self.children[c].startsWith(prefix[1:])
        else:
            return False
        
        