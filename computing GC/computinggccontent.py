#Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).

#Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated; please see the note on absolute error below.

# Read Data (FASTA)
from typing import final


def readFile(filePath):
    with open(filePath, "r") as f:
        return [l.strip() for l in f.readlines()]


txtfile = readFile("rosalind_gc.txt")
fastaDictonary = {}
fastaLabel = ""

finalDictLabel = ""
finalDict = {}

# Clean Data
for line in txtfile: 
    if ">" in line:
        fastaLabel = line
        fastaDictonary[fastaLabel] = ""
    else: 
               
        fastaDictonary[fastaLabel] += line

        finalDict[fastaLabel] = fastaLabel
             
        #Split Data by letter
        G = fastaDictonary[fastaLabel].count("G")
        C = fastaDictonary[fastaLabel].count("C")
        A = fastaDictonary[fastaLabel].count("A")
        T = fastaDictonary[fastaLabel].count("T")
        sum = G + C + A + T
        sumGC = G + C

        # Calculate Percent of GC 
        x = (sumGC / sum) * 100
        finalDict[fastaLabel] = x

# Get Label that belongs to the highest % Value
finalLabel = finalDict
maxLabel = max(finalLabel)
# Get Value that has the highest %
finalValue = finalDict.values()
maxValue = max(finalValue)

# Displays Label
print(maxLabel.split(">")[1])
# Displays Value
print(format(maxValue, ".6f"))



