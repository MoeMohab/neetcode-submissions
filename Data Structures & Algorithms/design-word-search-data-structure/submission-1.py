from collections import defaultdict
class WordDictionary:

    def __init__(self):
        self.children = defaultdict(WordDictionary)
        self.isWord = False

    def addWord(self, word: str) -> None:
        for char in word:
            self = self.children[char]
        self.isWord = True
    
    def search(self, word: str) -> bool:
        for i in range(len(word)):
            if word[i] == '.':
                newWord = ''.join(word[i+1:])
                return any([n.search(newWord) for c, n in self.children.items()])
            elif word[i] not in self.children:
                return False
            self = self.children[word[i]]
        return self.isWord

