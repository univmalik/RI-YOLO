''' 
Transforms bounding boxes associated text files to match with image rotation
'''

def finalString(intCList):
    outStr = ""
    outStr = outStr + str(intCList[0]) + " "
    for i in range(1, len(intCList), 1):
        if i % 5 == 0:
            outStr = outStr + "\n"
        outStr = outStr + str(intCList[i]) + " "

    return outStr

def rotatedList(valueList):
    # lists are by default passed by reference in Python
    # so we create a new list
    newList = valueList[:]

    for i in range(len(newList)):
        if i % 5 == 0:
            newList[i] = valueList[i]
        if i % 5 == 1:
            newList[i] = round(1 - valueList[i + 1], 4)
        if i % 5 == 2:
            newList[i] = round(valueList[i - 1], 4)
        if i % 5 == 3:
            newList[i] = round(valueList[i + 1], 4)
        if i % 5 == 4:
            newList[i] = round(valueList[i - 1], 4)

    return newList

# Integer cleaning for object
def IntCLIST(rotList):
    newList = rotList[:]
    for i in range(len(newList)):
        if i % 5 == 0:
            newList[i] = int(rotList[i])
        else:
            newList[i] = round(rotList[i], 4)

    return newList

# gets all values multiple of 5 in a Python list
def getValues(linestr):
    myIntegers = [float(x) for x in linestr.split()]
    return myIntegers

def outPutString(inputString):
    # first convert the string to a List
    outputList1 = getValues(inputString)
    outputList2 = rotatedList(outputList1)[:]
    outputList3 = IntCLIST(outputList2)[:]
    finalStr = finalString(outputList3)
    return finalStr

def rotTextC(fileNameTXT):
    file = open(fileNameTXT)

    newFileSize = len(fileNameTXT)
    newFileName = fileNameTXT[0:newFileSize - 4] + "-ROT90.txt"
    file2 = open(newFileName, "x")

    string = file.read()
    file2.write(outPutString(string))
    file2.close()

# play gymnastics here
def rotTextC180(fileNameTXT):
    file = open(fileNameTXT)

    if (fileNameTXT.find("-ROT90") != -1):
        newFileSize = len(fileNameTXT)
        newFileName = fileNameTXT[0:newFileSize - 10] + "-ROT180.txt"
        file2 = open(newFileName, "x")

        string = file.read()
        file2.write(outPutString(string))
        file2.close()

def rotTextC270(fileNameTXT):
    file = open(fileNameTXT)

    if (fileNameTXT.find("-ROT180") != -1):
        newFileSize = len(fileNameTXT)
        newFileName = fileNameTXT[0:newFileSize - 11] + "-ROT270.txt"
        file2 = open(newFileName, "x")

        string = file.read()
        file2.write(outPutString(string))
        file2.close()
