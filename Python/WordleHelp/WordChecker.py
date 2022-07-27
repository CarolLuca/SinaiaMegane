allLetters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

###
# Class owning the set of hints given in the course
# of playing one game of Wordle
class WordChecker:

    ###
    # Class constructor:
    def __init__(self):
        print(f"TODO: WordChecker is initialized")

        self._neededLetters = set({})
        self._wrongLetters = [set({}),set({}),set({}),set({}),set({})]
        self._goodLetters = ['','','','','']

    ###
    # Updates the internal state of the checker with a new hint
    def update(self, hint):
        print(f"TODO: WordChecker adding the hint: '{hint}'.")
        for i in {0,2,4,6,8}:
            if hint[i] == "-":
                self._wrongLetters[int(i/2)].add(hint[i+1])
            elif hint[i] == '+':
                self._goodLetters[int(i/2)] = hint[i+1]
                for c in allLetters:
                    if c != hint[i+1]:
                        self._wrongLetters[int(i/2)].add(c)
            else:
                self._wrongLetters[int(i/2)].add(hint[i+1])
                self._neededLetters.add(hint[i+1])


     ###
     # Checks whether a given word matches all known hints
    def check(self, word):
        print(f"TODO: WordChecker testing if '{word}' verifies all known hints.")

        for i in range(0,5):
            if word[i] in self._wrongLetters[i]:
                return False
        
        for c in self._neededLetters:
            if c not in word:
                return False

        return True
        
    ###
    # Returns a string representation of the entire object
    def __str__(self):
        return f"TODO: WordChecker internal state."

###
# WordChecker test code
if __name__ == "__main__":
    # creates a test WordChecker object and run through its methods
    wordChecker = WordChecker()
    wordChecker.update("-H+O+U+S~E")
    print(wordChecker.check("EOUST")) # COUST - False;  COUSE - False
    print(wordChecker)