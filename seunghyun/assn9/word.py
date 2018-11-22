import random

class Word:

    def __init__(self, filename):
        self.words = []
        self.wordlength = 0
        self.longestword = ""
        #self.longestwordlist = []
        f = open(filename, 'r')
        lines = f.readlines()
        f.close()

        self.count = 0
        for line in lines:
            word = line.rstrip()
            self.words.append(word)
            if len(word) > self.wordlength:
                self.wordlength = len(word)
                self.longestword = word
                #self.longestwordlist = []
            #elif len(word) == len(word):
                #self.longestwordlist += word
            self.count += 1

        print('%d words in DB' % self.count)


    def test(self):
        return 'default'


    def randFromDB(self, minLength):
        selected = False

        if self.wordlength < minLength:
            #return self.longestwordlist[1]
            return self.longestword
#제일 긴 단어가 여러개인 경우
        while not selected:
            r = random.randrange(self.count)
            if len(self.words[r]) >= minLength:
                selected = True
            else:
                continue
        return self.words[r]

