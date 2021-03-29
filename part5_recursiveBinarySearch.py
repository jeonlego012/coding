def recursiveBinarySearch(list, element_to_find, left, right):
    if left > right :
        return -1
    middle = (left+right)//2
    
    if list[middle] == element_to_find :
        return middle
    elif list[middle] > element_to_find :
        return recursiveBinarySearch(list, element_to_find, left, middle-1)
    else :
        return recursiveBinarySearch(list, element_to_find, middle+1, right)

print(recursiveBinarySearch([2, 5, 7, 9, 11, 14, 15, 16, 17, 18], 17, 0, 9))