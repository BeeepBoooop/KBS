from flask import Flask, render_template, request, jsonify
from model.knowledge import Knowledge
from parsers.knowledgeParser import KnowledgeBaseParser
"""-------------------------------------------Logic----------------------"""
"""Khai báo"""
matchedTargets = list()
matchesRules = dict()
userInput = Knowledge()
knowledgeBaseFile = ".\data\knowledge.json"
knowlages = KnowledgeBaseParser()
knowlageBase = knowlages.getKnowledgeBase(knowledgeBaseFile)
checklist= list()
"""Làm mới"""
def renew():
    matchedTargets.clear()
    matchesRules.clear()
    userInput.clearRules()
    checklist.clear()
def updateBase(path):
     global knowlageBase
     knowlage = KnowledgeBaseParser()
     global knowledgeBaseFile
     knowlageBase = knowlage.getKnowledgeBase(path)
     knowledgeBaseFile = path
"""kiểm tra và thêm luật"""
def checkDuplicate(ruleUser):
    for i in checklist:
        if( i.getRule() in ruleUser):
            return "a"
    return "b"

def add():
    matchedTargets.clear()
    for know in knowlageBase:
        for rule in know.getRules():
            for user in userInput.getRules():
                if rule == user:
                    matchedTargets.append(know)
                    checklist.append(rule)
                    break

    matchesRules_temp = dict()
    for matchedTarget in matchedTargets:
            match = 0
            for rule in matchedTarget.getRules():
                for userRule in userInput.getRules():
                    if rule == userRule:
                        match += 1
            matchesRules_temp[matchedTarget.getTarget()] = round((match / len(matchedTarget.getRules())) * 100)
    matchesRules_temp = sorted(matchesRules_temp.items(), key = lambda item : -item[1])
    matchesRules = matchesRules_temp
    return matchesRules

def addForPropose() :
    matchedTargets.clear()
    ds = list()
    for know in knowlageBase:
        ds.append(know.getOneRule())
        for rule in know.getRules():
            for user in userInput.getRules():
                if(rule == user):
                    matchedTargets.append(know)
                    break
    if len(matchedTargets) == 0:
        return ds[0:4]
    matchKnowledge = {}
    for matchedTarget in matchedTargets:
            match = 0
            for rule in matchedTarget.getRules():
                for userRule in userInput.getRules():
                    if rule == userRule:
                        match += 1
            matchKnowledge[matchedTarget] = round((match / len(matchedTarget.getRules())) * 100)
    return matchKnowledge
"""trả lời"""
def askQuestion(mess):
    if(mess.strip() == "bye"):
        renew()
        return ""
    input = mess.split(",")
    for u in input:
        if(checkDuplicate(u)== 'b'):
            userInput.addRule("user",u.lower())
    return add()
"""Đề xuất"""
def getProposes():
    proposes = list()
    count_target = 0
    if (type(addForPropose()) != dict):
        return addForPropose()
    targets = list(sorted(addForPropose().items(), key=lambda item : -item[1]))
    if (len(targets) >=2) :
        while (count_target < 2) :
            proposes.append(targets[count_target][0].getOneRule())
            proposes.append(targets[count_target][0].getOneRule())
            proposes.append(targets[count_target][0].getOneRule())
            proposes.append(targets[count_target][0].getOneRule())
            count_target +=1
    else :
        proposes.append(targets[count_target][0].getOneRule())
        proposes.append(targets[count_target][0].getOneRule())
        proposes.append(targets[count_target][0].getOneRule())
    proposes_list = list(set(proposes))
    input = userInput.getRules()
    
    for value in proposes_list :
        if(value in input) :
            proposes_list.remove(value)
    return proposes_list
def getDC(key):
    for i in knowlageBase:
        if(i.getTarget()== key):
            return i.getSolution()
    return
"""-------------------------------------------Logic----------------------"""

app = Flask(__name__)
@app.route("/")
def home_1():
    renew()
    return render_template('home.html')

@app.route("/ask")
def home():
    type = request.args['type']
    global knowledgeBaseFile
    renew()
    if(type == "1"):
     updateBase(".\data\knowledge.json")
    if(type == "2"):
     updateBase(".\data\knowledge.json")
    if(type == "3"):
      updateBase(".\data\knowledge.json")
    if(type == "4" ):
     updateBase(".\data\knowledge.json")
    if(type == "5"):
        updateBase(".\data\knowledge.json")
    return render_template('index.html')

@app.route("/get")
def getResponse():
    message = str(request.args['message'])
    message = message.replace("và",",")
    reply = askQuestion(message)
    return jsonify(reply)

@app.route("/getPropose")
def getPropose():
    list_proposes = getProposes()
    return ", ".join(list_proposes)

@app.route("/dieuchi")
def getDieuchi():
    key = request.args['linkdc']
    dc = getDC(key)
    return render_template('dieutri.html', dieuchibenh = dc, tenbenh = key)
@app.route("/getResult")
def getResult():
    if(len(matchedTargets) == 0):
        return "đi khám tổng quát"
    else:
       return "có thể bạn đã bị "+ matchedTargets[0].getTarget()
    
if __name__ == "__main__":
    app.run(debug=True)