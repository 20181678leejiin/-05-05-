class Guess:

    def __init__(self, word):
        self.numTries =0
        self.secretWord = word
        self.currentStatus:"_"*len(word)
        self.guessedChars = []
        self.guess('') # 이거 왜 넣어요?


    def display(self):
        guessWord = ''
        for c in self.currentStatus:
            guessWord += (c+'')
        return guessWord

        guessed = ''
        for c in sorted(list(self.guessedChars)):
            guessed += (c+'')
        return guessed

    def guess(self, character):

        self.guessedChars.append(character)
        if character not in self.secretWord:
            return False

        else:
            currentStatus = ''
            for c in self.secretWord:
                self.numTries +=1
                if c in self.guessedChars:
                    currentStatus +=c
                else:
                    currentStatus += "_"

            self.currentStatus = currentStatus

            return True

