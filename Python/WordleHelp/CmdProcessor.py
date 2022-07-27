import os
import re

###
# Class CmdProcessor is in charge of implementing all commands supported by WordleHelp
from WordChecker import WordChecker

class CmdProcessor:
    ###
    # Class fields
    # _wordChecker: the "engine" in charge of storing and using all hints
    #               used for verifying words from the database

    ###
    # Class constructor
    def __init__(self):
        self._wordChecker = WordChecker()
        self._dictionary = {}

    def processHelp(self):
        print("process command 'help'")

    def processAdd(self, args = None):
        print("Process command 'add'")
        
        if args == None:
            raise Exception(f"Missing or invalid argument '{args}'. Expected file path!")
        filePath = args
        if not os.path.isfile(filePath):
            raise Exception(f"File {filePath} cannot be located!")
        
        lines = open(filePath)
        for line in lines:
            pair = re.split("\t", line)
            key = str(pair[0])
            val = int(pair[1])
            self._dictionary[key] = val
        
        # print(self._dictionary)

    def processMatch(self, args = None):
        print("Process command 'match'")

        if args == None:
            raise Exception(f"Missing or invalid argument '{args}'. Expected file path!")
        hint = args

        good_words = {}
        self._wordChecker.update(hint)
        for word in self._dictionary:
            if self._wordChecker.check(word):
                good_words[word] = self._dictionary[word]
        
        return good_words


    
    def processReset(self, args = None):
        print("Process command 'reset'")

    def processStats(self, args = None):
        print("Process command 'stats'")

    def processConfig(self, args = None):
        print("Process command 'config'")

###
# CmdProcessor test code
if __name__ == "__main__":
    cmdP = CmdProcessor()
    cmdP.processHelp()
    cmdP.processAdd("Python\WordleHelp\words.txt")


    # + verde
    # - negru
    # ~ galben