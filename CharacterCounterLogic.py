import turtle as t

def characterCounter (inputString, charHistogram):
    # If the char currently being parsed is in the dictionary, increment its associated value-pair by 1
    # otherwise append the char to the dictionary and initialize its associated value-pair with 1
    for char in inputString:
        if char in charHistogram:
            charHistogram[char] += 1
        else:
            charHistogram[char] = 1

def totalChars (histogramList):
    # Return the total sum of frequencies of all characters
    return sum(histogramList[n][1] for n in range (len(histogramList)))

def partialChars(histogramList, numOfSlices):
    # Return the sum of frequency of characters of the first N most frequent characters
    return sum(histogramList[n][1] for n in range (numOfSlices))

def genColorList(numOfSlices):
    # A predefined list of 50 unique colors that are used to fill the pie slice
    # returns N + 1 colors in order to accommodate for the "All other Characters" slice
    colors = ["#d0d8a4", "#77e9dd", "#3c883d", "#7286f9", "#c94d14", "#f18f78", "#a4740a", "#20b6ab", "#9bfb25", "#6fe05b",
              "#429451", "#27ea1e", "#e5f1b2", "#1b92c4", "#3cd80a", "#eb19b0", "#c7afac", "#d4c560", "#6af8a2", "#cf1465",
              "#b35049", "#82ff30", "#5590b0", "#1d9139", "#92a1e2", "#ed9e7d", "#199bc5", "#2dc06c", "#f31160", "#c14459",
              "#c5d998", "#4760c6", "#80e7b4", "#7ba0a3", "#ab1fc6", "#682bc2", "#0f4f96", "#1a03d7", "#55ce4c", "#d16ccd",
              "#380802", "#24b7ed", "#14a0e6", "#88bc6b", "#e30f51", "#afb40a", "#e093b3", "#cf747f", "#9b11bd", "#f4fcbb"]
    return colors[:numOfSlices+1]

def genSortedFrequency(fileName):
    # Read a text file and generate a 2-tuple frequency list that is sorted
    # by the frequencies of the most common characters
    charHistogram = {}
    file = open (fileName)
    for line in file:
        characterCounter(line, charHistogram)

    # Sort the keys of the dictionary according to their frequency
    sortedKeys = sorted(charHistogram, key=charHistogram.__getitem__, reverse=True)

    # Generate a list of tuples of characters and their frequencies
    sortedFreq = [(char, charHistogram[char]) for char in sortedKeys]
    return sortedFreq

def genFreqPercentage (histogramList, numOfSlices):
    # Return a 2-tuple list that contains the characters and their percentages of occurrences
    # find ht e
    totalSumOfChars = totalChars(histogramList)
    partialSumOfChars = partialChars(histogramList, numOfSlices)

    percentageList = [(histogramList[n][0], round((histogramList[n][1]/totalSumOfChars), 5)) for n in range(numOfSlices)]
    percentageList.append(("All other characters", round((totalSumOfChars - partialSumOfChars)/totalSumOfChars, 5)))

    return percentageList


def genPieChart (piechart, sliceColor, radius):
    assert (len(piechart) == len(sliceColor))
    t.reset()
    t.penup()
    t.goto (0, -300)
    t.pendown()
    t.circle(radius)
    print(len(piechart))
    for i in range(len(piechart)):
        sliceDegree = piechart[i][1]*360
        sliceLabel = piechart[i][0]

        if sliceLabel == ' ':
            sliceLabel = "'space'"
        else:
            sliceLabel = "'" + sliceLabel + "'"

        t.color(sliceColor[i])
        t.begin_fill()
        t.circle(radius, (sliceDegree))
        t.left(90)
        t.forward(radius)
        t.left(-(sliceDegree) + 180)
        t.forward(radius)
        t.end_fill()
        t.left(90)
        t.circle(radius, (sliceDegree))
        t.right(90)
        t.fd(150)
        t.color("black")
        t.write(sliceLabel + ', ' + str(round((piechart[i][1]*100),2)) + '%', False, "left", ("Arial", 14, "normal"))
        t.color(sliceColor[i])
        t.backward(150)
        t.left(90)
    t.mainloop()

def drawPieChart (fileName, numOfSlices):
    charFrequency = genSortedFrequency(fileName)
    charPercentage = genFreqPercentage(charFrequency, numOfSlices)
    print(charPercentage)
    sliceColors = genColorList(numOfSlices)
    genPieChart(charPercentage, sliceColors, 350)