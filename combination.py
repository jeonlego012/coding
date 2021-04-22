from itertools import combinations

n, m = map(int, input().split())
numbers = [number for number in range(1,n+1)]

combination = list(combinations(numbers, m))

for i in range(len(combination)) :
    for comb in combination[i] :
        print(comb, end=' ')
    print()