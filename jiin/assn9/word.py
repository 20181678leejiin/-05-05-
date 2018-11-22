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

        print('%d words in DB' % self.count)


    def test(self):
        return 'default'


    def randFromDB(self,minLenght):
        selected = False
        if 22<minLenght: # 최대 길이가 22인것을 알고있음! 모를경우 대비하기
            minLenght = 22

        while not selected:
            r = random.randrange(self.count)
            if len(self.words[r]) <= minLenght:
                self.randFromDB(minLenght)
            else:
                return self.words[r] # 길이가 1개 인경우 가장 긴 단어가 2개 이상일 경우 생각하기!

