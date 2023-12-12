"""
The parsed output of the knowledge,json is used to create
the Knowledge object consisting of the target and rules
"""
import random

class Rule:
    """
    Class to store the rule in the string format

    Attributes
    -----------
    __rule: str
        rule for the knowledge
    """

    def __init__(self, rule: str):
        self.__rule = rule

    def getRule(self):
        return self.__rule

    def __eq__(self, other):
        if other.__rule.__contains__(self.__rule):
            return True
        return False

    def __str__(self):
        """
        Print the rule string

        Returns
        -------
        str
            rule
        """
        return self.__rule


class Knowledge:
    """
    Class that connects the target with the rules (Rule objects).

    Attributes
    ----------
    __target : str
        name of the target or the output
    __rules : list
        list of the Rule objects

    """

    def __init__(self):
        self.__target = None
        self.__rules = list()
        self.__solution = None

    def addRule(self, target, rule):
        self.__target = target
        self.__rules.append(Rule(rule))
    def addSolution(self, solution):
        self.__solution = solution
    def __str__(self):
        data = list()
        data.append(self.__target)
        data.append(" =====> \n")
        for rule in self.__rules:
            data.append("\t  <<< ")
            data.append(rule.getRule())
            data.append(" >>>  \n")
        data.append("\n\n")

        return "".join(data)

    def getTarget(self):
        return self.__target

    def getRules(self):
        return self.__rules
    def clearRules(self):
        self.__rules= list()
    def getOneRule(self):
        return random.choice(self.__rules).getRule()
    def getSolution(self):
        return self.__solution
