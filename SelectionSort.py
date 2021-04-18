arrObj = [7,4,10,8,3,1]

def selectionSort(arr):
    """Performing selection sort"""
    for i in range(0,len(arr)):
        minIndex = i
        for j in range(i+1, len(arr)):
            if arr[minIndex] > arr[j]:
                minIndex = j
        
        """swap i index value in minIndex value"""
        temp = arr[i]
        arr[i] = arr[minIndex]
        arr[minIndex] = temp 
        print(arr)
        print("\n")

    return arr

sortedArray = selectionSort(arrObj)
print(sortedArray)         
