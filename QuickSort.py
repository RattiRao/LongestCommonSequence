arrObj = [7,6,10,5,9,2,1,15,7]

def sort(lb, ub):
    pivot = arrObj[lb]
    start = lb
    end = ub
    
    while (start < end):
        """ """
        while(arrObj[start] <= pivot):
            start += 1
            if start < len(arrObj):
                break

        while(arrObj[end] > pivot):
            end -= 1
        
        if start < end :
            """swap start end value"""
            temp = arrObj[start]
            arrObj[start] = arrObj[end]
            arrObj[end] = temp

    
    """ swap pivot value with end value"""
    temp = arrObj[lb]
    arrObj[lb] = arrObj[end]
    arrObj[end] = temp

    return end

def quickSort(lb, ub):
    if lb < ub:
        loc = sort(lb,ub)
        quickSort(lb, loc-1)
        quickSort(loc+1, ub)
    

quickSort(0,8)
print(arrObj)

            
    
    
    
    
    