
def findLongestCommonSubsequnce(input1, input2):
    """Finding longest common sequence"""

    arrInput = createEmptyArray(len(input1), len(input2))
    print(arrInput)
    for i in range(0,len(input1)):
        for j in range(0, len(input2)):
            if i > 0 and j > 0:
                if input1[i] == input2[j]:
                    arrInput[i][j] = 1 + arrInput[i-1][j-1]
                else:
                    arrInput[i][j] = max(arrInput[i-1][j], arrInput[i][j-1])
        
    return arrInput[len(input1)-1][len(input2) - 1]

            


    

def createEmptyArray(size, rows):
    listObj = [0]*size
    listObj = [listObj]*rows
    print(listObj)
    return listObj

    
result = findLongestCommonSubsequnce("abaaba", "babbab")
print(result)



