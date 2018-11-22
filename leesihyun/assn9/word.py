import random

class Word:

    def __init__(self, filename):
        self.words = []
        f = open(filename, 'r')
        lines = f.readlines()
        f.close()

        self.count = 0
        for line in lines:
            word = line.rstrip()
            self.words.append(word)
            self.count += 1

        self.words = sorted(self.words,key = lambda p:len(p))
        print(self.words)
        print('%d words in DB' % self.count)


    def test(self):
        return 'default'

    def lower_bound(self,minLength):
        s = 0
        e = len(self.words)-1
        while(s<e):
            m = (s + e)//2
            if len(self.words[m])<minLength:
                s = m + 1
            else:
                e = m
        return s
    def randFromDB(self,minLength):
        if minLength>len(self.words[-1]):
            minLength = len(self.words[-1])

        idx = self.lower_bound(minLength)
        r = random.randrange(idx,len(self.words))
        return self.words[r]

if __name__ == "__main__":
    a = Word("words.txt")
    print(a.lower_bound(3))