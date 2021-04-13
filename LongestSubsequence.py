import enum

class SubsequenceArrow(enum.Enum):
    """ Enum for directions"""
    left = "left"
    top = "top"
    diagonal = "diagonal"
    none = "none"

class Subsequence:
    """Subsequence class"""
    value = 0
    info = ""
    direction = SubsequenceArrow.none




def findLongestCommonSubsequence(input1, input2):
    """Finding longest common sequence"""
    strValue = ""
    listInput1 = list(input1)
    listInput2 = list(input2)
    arrInput = createEmptyArray(len(listInput1), len(listInput2))
    print(arrInput)
    for i in range(1,len(listInput1)+1):
        for j in range(1, len(listInput2)+1):
            (arrInput[i][j]).info = listInput1[i-1]
            if listInput1[i-1] == listInput2[j-1]:
                    updatedValue =  (1 + (arrInput[i-1][j-1]).value)
                    (arrInput[i][j]).value = updatedValue
                    arrInput[i][j].direction = SubsequenceArrow.diagonal
                    print(updatedValue)
            else:
                if arrInput[i-1][j].value > arrInput[i][j-1].value:
                    arrInput[i][j].direction = SubsequenceArrow.top
                else:
                    arrInput[i][j].direction = SubsequenceArrow.left
                
                (arrInput[i][j]).value = max(arrInput[i-1][j].value, arrInput[i][j-1].value)
                print((arrInput[i][j]).value)
        
        print("\n")
    getSubsequenceString(arrInput, len(listInput1)-1, len(listInput2) - 1)  
    return arrInput[len(listInput1)][len(listInput2)].value


def createEmptyArray(size, rows):
    listFinal = list()
    for i in range(0,rows+1):
        listObj = list()
        for j in range(0, size+1):
            obj = Subsequence()
            listObj.append(obj)
        listFinal.append(listObj)

    print(len(listFinal[5]))
    return listFinal

def getSubsequenceString(listObj, i, j):
    if i == 0 and j == 0:
        return
    if listObj[i][j].direction == SubsequenceArrow.left:
        getSubsequenceString(listObj, i, j-1)

    elif listObj[i][j].direction == SubsequenceArrow.diagonal:
        print(listObj[i][j].info)
        getSubsequenceString(listObj, i-1, j-1)

    elif listObj[i][j].direction == SubsequenceArrow.top:
        print(listObj[i][j].info)
        getSubsequenceString(listObj, i-1, j)

        



# def getLongestCommonSubsequenceString(listParam):
#     """ Get string value """
#     listObj = list(listParam)

#     for i in Range(len((listObj) - 1), 0, -1):
#         for j in Range(len((listObj) - 1), 0, -1):





result = findLongestCommonSubsequence("abaaba", "babbab")
print(result)



