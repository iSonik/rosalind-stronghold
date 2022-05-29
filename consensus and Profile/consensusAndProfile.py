# Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.

# Return: A consensus string and profile matrix for the collection. (If several possible consensus strings exist, then you may return any one of them.)

# Sample Dataset
# >Rosalind_1
# ATCCAGCT
# >Rosalind_2
# GGGCAACT
# >Rosalind_3
# ATGGATCT
# >Rosalind_4
# AAGCAACC
# >Rosalind_5
# TTGGAACT
# >Rosalind_6
# ATGCCATT
# >Rosalind_7
# ATGGCACT

# Sample Output
# ATGCAACT
# A: 5 1 0 0 5 5 0 0
# C: 0 0 1 4 2 0 6 1
# G: 1 1 6 3 0 1 0 0
# T: 1 5 0 0 0 1 1 6



def readFile(filePath):
    with open(filePath, "r") as f:
        return [l.strip() for l in f.readlines()]

list_A = []
list_C = []
list_G = []
list_T = []

sampleDict = {}
sampleLabel= ""


txtfile = readFile("rosalind_cons.txt")

for line in txtfile: 
    if ">" in line:
        sampleLabel = line
        sampleDict[sampleLabel] = ""
    else: 
               
        sampleDict[sampleLabel] += line


for dic in sampleDict:
    #Get Length of String and remove \n
    x = sampleDict[dic]
    xLen = len(x)
 


for i in range(0, xLen):
    # Create 4 lists each with the length of the String
    list_A.append(0)
    list_C.append(0)
    list_G.append(0)
    list_T.append(0)


for dic in sampleDict:
        for i in range(0, xLen):
            if sampleDict[dic][i] == "A":
                list_A[i] = list_A[i] + 1
            if sampleDict[dic][i] == "C":
                list_C[i] = list_C[i] + 1
            if sampleDict[dic][i] == "G":
                list_G[i] = list_G[i] + 1
            if sampleDict[dic][i] == "T":
                list_T[i] = list_T[i] + 1



count = 0
finalString = ""

# # print(len(list_A))
for x in range(len(list_A)):
    A =list_A[count]
    C =list_C[count]
    G =list_G[count]
    T =list_T[count]
    currentDict = {"A": A, "C": C,"G": G, "T":T}
    finalString= finalString + (max(currentDict, key=currentDict.get))
    count = count + 1


# Formating for String to Format: A: 5 1 0 0 5 5 0 0
string_A = f"A: {' '.join([str(item) for item in list_A])}"
string_C = f"C: {' '.join([str(item) for item in list_C])}"
string_G = f"G: {' '.join([str(item) for item in list_G])}"
string_T = f"T: {' '.join([str(item) for item in list_T])}"


print(string_A)
print(string_C)
print(string_G)
print(string_T)

