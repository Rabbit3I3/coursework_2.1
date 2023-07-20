class BasicWord:
    def __init__(self, word, subwords):
        self.word = word
        self.subwords = subwords

    def check_input(self, word):
        return word in self.subwords

    def __repr__(self):
        return self.word


    def count_subwords(self):
        return len(self.subwords)


