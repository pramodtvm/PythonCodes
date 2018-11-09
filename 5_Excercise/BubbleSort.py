a = [3,2,1,9,4,77,11,4]

count = 0
def bubblesort(a):
    for i in range(len(a)):
        swamp = True
        for j in range(0,len(a)-1):
            if a[j] > a[j+1]:
                swamp = False
                global count
                count +=1
                a[j],a[j+1] = a[j+1],a[j]


        if  swamp == True:
            break

bubblesort(a)
print("prnting array",a)
print("prnting Count", count)