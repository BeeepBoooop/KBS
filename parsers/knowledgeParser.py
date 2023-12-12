import json
import os

from model.knowledge import Knowledge

class KnowledgeBaseParser:

    def __init__(self):
        self.__knowledgeBase = list()

    def __parseInputFile(self, inputFile):
        # checking if the file exists
        if os.path.isfile(inputFile) is False:
            return

        # reading the file
        with open(inputFile, "r", encoding="utf-8") as file:
            file = json.load(file)

            for knowledge in file['target']:
                knowledgeBase = Knowledge()
                for rule in knowledge['rules']:
                    knowledgeBase.addRule(target=knowledge['name'],
                                          rule=knowledge['rules'][rule]
                                          )
                    knowledgeBase.addSolution(solution=knowledge['solution'])
                self.__knowledgeBase.append(knowledgeBase)

        return self.__knowledgeBase

    def getKnowledgeBase(self, inputFile):
        return self.__parseInputFile(inputFile)
