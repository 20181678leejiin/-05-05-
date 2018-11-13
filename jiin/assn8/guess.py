class Guess:

    def __init__(self, word):

        self.secretWord = word
        self.currentStatus = '_' * len(word)
        self.guessedChars = set()

    def guess(self, character):
        self.guessedChars.add(character)
        if character not in self.secretWord:
            return False
        else:
            currentStatus = ''
            for c in self.secretWord:
                if c in self.guessedChars:
                    currentStatus += c
                else:
                    currentStatus += '_'

            self.currentStatus = currentStatus
            return True

    def displayCurrent(self):

        guessdWord = ''
        for c in self.currentStatus:
            guessdWord += (c + ' ')
        return guessdWord

    def displayGuessed(self):

        guessed = ''
        for c in sorted(list(self.guessedChars)):
            guessed += (c + ' ')
        return guessed

    def finished(self):
        if self.currentStatus == self.secretWord:
            return True
        else:
            return False