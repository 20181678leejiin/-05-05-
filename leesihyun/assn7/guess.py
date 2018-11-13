class Guess:

    def __init__(self, word):
        self.numTries = 0
        self.guessedChars = set()
        self.secretWord = word
        self.currentStatus = '_'*len(word)
        self.idx = [[] for i in range(0,26)]
        self.pre_process(word)
        self.success_num=0
        pass

    def pre_process(self,word):
        num_a = ord('a')
        for i in range(len(word)):
            num_i = ord(word[i])
            self.idx[num_i - num_a].append(i)
        pass

    def display(self):
        print("Current: %s"%(self.currentStatus))
        print("Already Used: ",end="")
        for i in self.guessedChars:
            print(i,end=" ")
        print()
        print("Tries: %d"%(self.numTries))
        pass


    def guess(self, character):
        self.guessedChars.add(character)
        num_char = ord(character)
        num_a = ord('a')
        if len(self.idx[num_char - num_a])==0:
            self.numTries+=1
            return False

        for i in self.idx[num_char - num_a]:
            self.currentStatus = self.currentStatus[:i]+character+self.currentStatus[i+1:]
        self.success_num+=len(self.idx[num_char - num_a])
        if self.success_num == len(self.secretWord):
            return True

        pass
