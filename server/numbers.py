numbers = map(int,input().split())
for num in numbers:
    if num%2 == 0 :
        print (f"{num} - число четное")
    else:
        print (f"{num} - число НЕчетное")
