def binarySearch(list, element_to_find):
    left = 0
    right = len(list) - 1
    while left<=right :
        middle = (left+right)//2
        if list[middle] == element_to_find :
            return middle
        elif list[middle] > element_to_find :
            right = middle - 1
        else :
            left = middle + 1
    return -1
            