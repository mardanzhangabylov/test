numbers = map(int,input().split())
for num in numbers:
    #num = int(num)
    if num%2 == 0 :
        print (f"{num} - число четное")
    else:
        print (f"{num} - число НЕчетное")
