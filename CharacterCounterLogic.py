def characterCounter (inputString):
    charsDict = {}
    for char in inputString:
        if char in charsDict:
            charsDict[char] += 1
        else:
            charsDict[char] = 1
    print(charsDict)

characterCounter("Branches is too leafy")