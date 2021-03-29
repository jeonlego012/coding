def recursive_fibonacci(number) :
    if number == 1 or number == 2 :
        return 1
    else :
        return recursive_fibonacci(number-1) + recursive_fibonacci(number-2)

def iterative_fibonacci(number) :
    n = 0
    for i in range(1, number+1):
        if i == 1 :
            first = 1
        elif i == 2:
            second = 1
        else :
            first, n = second, first+second
            #n = first+second
            #first = second
            second = n
    return n


print(recursive_fibonacci(5))
print(iterative_fibonacci(5))