import random
import speech_recognition as sr
import pyttsx3
from chatGPT import ChatGPT

filename = "dialogue_testing.txt"
current_rule = None
rules = []
var_rules = []
options = []
vars = []

class Rule:
    def __init__(self, name):
        self.name = name
        self.responses = []
        self.has_var = False
        self.v = ""
        self.subrules = []
    
    def select(self):
        if(len(self.responses) == 1):
            return self.responses[0]
        num = random.randint(0, len(self.responses) - 1)
        return self.responses[num]
    
    def addSubrule(self, rule):
        self.subrules.append(rule)

    def getSubrules(self):
        return self.subrules
    
    def addResponse(self, r):
        self.responses.append(r)
        #print("Added response: " + r)
    
    def addVar(self, val):
        self.has_var = True
        self.v = val
    
    def getVar(self):
        return self.v
    
    def hasVar(self):
        return self.has_var
    
    def getName(self):
        return self.name

class Variable:
    def __init__(self, name):
        self.name = name
        self.val = ""
    
    def getName(self):
        return self.name
    
    def getVal(self):
        return self.val
    
    def setVal(self, v):
        self.val = v

class Option:
    def __init__(self, name):
        self.name = name
        self.o = []
        self.subrules = []

    def addOptions(self, options):
        for op in options:
            self.o.append(op)
        #print("Added Options: " + str(self.o))

    def getOptions(self):
        return self.o
    
    def getName(self):
        return self.name
    
    def addSubrule(self, rule):
        self.subrules.append(rule)
    
    def getSubrules(self):
        return self.subrules



def parse(line, num):
    line = line.lower()
    start = line[0]


    if(start == '#' or '#' in line):
        return
    elif(start == '~'):
        #Create Option object with name
        index = line.index(':')
        name = line[1:index]
        #print("Creating new option with name: " + name)
        op = Option(name)

        #Find option values to add to object
        brac_start = line.index('[')
        brac_end = line.index(']')
        opts = line[brac_start + 1:brac_end]
        opts = parseOptions(opts)
        #print(opts)
        op.addOptions(opts)
        options.append(op)

    elif(start == 'u'):
        has_var = False
        #Find input values
        strs = line.split(':')
        if(len(strs) < 3):
            print("Error on line " + str(num))
            return
        paren = strs[1]
        input = paren[1:-1]
        if('(' in input):
            input = input.replace('(', '')
        if(')' in input):
            input = input.replace(')', '')
        if(input[0] == '~'):
            input = input[1:]

        r = Rule(input)
        #print("New rule created: " + input)
        if('_' in input):
            has_var = True
            #print("This rule has a var")

        #Find Responses
        response = strs[2]
        if('[' in response):
            brac_start = line.index('[')
            brac_end = line.index(']')
            opts = line[brac_start + 1:brac_end]
            opts = parseOptions(opts)
            for o in opts:
                r.addResponse(o)
        else:
            r.addResponse(response)

        #Check for vars
        if('$' in line):
            index = line.index('$')
            name = ""
            while(line[index] != ' '):
                name = name + line[index]
                if(index == len(line) - 1):
                    break
                index += 1
            if not name in vars:
                v = Variable(name.strip())
                vars.append(v)
                if(has_var):
                    r.addVar(v)

        if(has_var):
            var_rules.append(r)
        else:
            rules.append(r)
        global current_rule 
        current_rule = r

    elif(start == '\t' or start == ' '):
        current = line[0]
        count = 0
        while(current == '\t' or current == ' '):
            count += 1
            current = line[count]
        line = line[count:]
        start = line[count]
        has_var = False
        #Find input values
        strs = line.split(':')
        if(len(strs) < 3):
            print("Error on line " + str(num))
            return
        paren = strs[1]
        input = paren[1:-1]
        if('(' in input):
            input = input.replace('(', '')
        if(')' in input):
            input = input.replace(')', '')
        if(input[0] == '~'):
            input = input[1:]

        r = Rule(input)
        #print("New rule created: " + input)
        if('_' in input):
            has_var = True
            #print("This rule has a var")

        #Find Responses
        response = strs[2]
        if('[' in response):
            brac_start = line.index('[')
            brac_end = line.index(']')
            opts = line[brac_start + 1:brac_end]
            opts = parseOptions(opts)
            for o in opts:
                r.addResponse(o)
        else:
            r.addResponse(response)

        #Check for vars
        if('$' in line):
            index = line.index('$')
            name = ""
            while(line[index] != ' '):
                name = name + line[index]
                if(index == len(line) - 1):
                    break
                index += 1
            if not name in vars:
                v = Variable(name.strip())
                vars.append(v)
                if(has_var):
                    r.addVar(v)
        #print("Added " + r.getName() + " as a SR of " + current_rule.getName())
        current_rule.addSubrule(r)
            
    else:
        print("Error on line " + str(num) + ": Unrecognized starting character.")
        pass

def parseOptions(options):
    ret = []
    opts = options.split()
    while(len(opts) > 0):
        current = opts[0]
        if(current[0] == '"'):
            if(len(opts) > 1):
                temp = opts[1]
                if(temp[len(temp) - 1] == '"'):
                    choice = current[1:] + ' ' + temp[0:-1]
                    ret.append(choice)
                    opts.remove(current)
                    opts.remove(temp)
                else:
                    print("Error: No terminating quote")
            else:
                print("Error: No terminating quote")
        else:
            ret.append(current)
            opts.remove(current)
    #print("Finished parsing options: " + str(ret))
    return ret

def readFile():
    #print("Starting parse...")
    file = open(filename, 'r')
    lines = file.readlines()
    count = 0
    for line in lines:
        #print("Parsing: " + line)
        parse(line, count)
        count+=1

def findRuleByName(name):
    for rule in rules:
        #print("RULE: Comparing " + rule.getName() + " and " + name)
        if(rule.getName().strip() == name.strip()):
            return rule
    return -1

def getResponse(word):
    global current_rule
    #print("CR: " + current_rule.getName())
    subrules = current_rule.getSubrules()
    if(len(subrules) != 0):
        #print("Found subrules...")
        for sub in subrules:
            if(sub.hasVar()):
                #print("Found subrules with var...")
                rule = sub.getName()
                #print("Checking " + rule)
                r_split = rule.split()
                w_split = word.split()
                if(len(r_split) == len(w_split)):
                    count = 0
                    for s in r_split:
                        if '_' in s:
                            val = w_split[count]
                            var = sub.getVar()
                            var.setVal(val)
                            return sub.select()
                        else:
                            if(r_split[count] != w_split[count]):
                                break
                        count += 1
            else:
                if(word.strip() == sub.getName().strip()):
                    return sub.select()

    result = findRuleByName(word)
    if(result != -1):
        current_rule = result
        return result.select()
    

    for o in options:
        ops = o.getOptions()
        for op in ops:
            #print("Comparing " + op + " and " + word)
            if(op == word):
                #print("Match found")
                name = o.getName()
                #print("Searching rules for " + name)
                result = findRuleByName(name)
                if(result != -1):
                    current_rule = result
                    return result.select()
    for vr in var_rules:
        rule = vr.getName()
        r_split = rule.split()
        w_split = word.split()
        if(len(r_split) == len(w_split)):
            count = 0
            for s in r_split:
                if '_' in s:
                    val = w_split[count]
                    var = vr.getVar()
                    var.setVal(val)
                    current_rule = vr
                    return vr.select()
                else:
                    if(r_split[count] != w_split[count]):
                        break
                count += 1

    ai = ChatGPT()
    response = ai.question_random(word)
    
    return(response) # REPLACE WITH AI BACKEND 

def getVarValue(name):
    #print(str(vars))
    for v in vars:
        #print("Comparing " + name + " and " + v.getName())
        if(v.getName() == name):
            #print("Found match")
            return str(v.getVal())
    return ""

def checkResponse(line):
    ret = ""
    if('$' in line):
        strs = line.split()
        for s in strs:
            if('$' in s):
                ret = ret + getVarValue(s) + " "
            else:
                ret = ret + s + " "
        return ret
    else:
        return line

def pickGreeting():
    greetings = ["hello", "howdy", "hi there"]
    return greetings[random.randint(0,2)]

def final(display):
    engine = pyttsx3.init()
    readFile()
    listening = True

    greeting = pickGreeting()
    print("Robot: " + greeting)
    display.printText(greeting, 30)
    engine.say(greeting)
    engine.runAndWait()

    while listening:
        print("Human: ")
        word = input()
        response = getResponse(word.strip())
        response = checkResponse(response)
        if("office" in response):
            engine.say("Okay! Follow me...")
            engine.runAndWait()
            return 2
        elif("restrooms" in response):
            engine.say("Okay! Follow me...")
            engine.runAndWait()
            return 3
        else:
            print("Robot: " + response)
            engine.say(response)
            engine.runAndWait()
            display.printText(word + "\n\n" + response, 20)
            

def begin():
    global current_rule
    listening = True
    while listening:
        with sr.Microphone() as source:
            r= sr.Recognizer()
            r.adjust_for_ambient_noise(source)
            r.dyanmic_energythreshhold = 3000

            print("Human: ")
            word = input()
            response = getResponse(word.strip())
            response = checkResponse(response)
            
            print("Robot: " + response)


if __name__ == "__main__":
    final()