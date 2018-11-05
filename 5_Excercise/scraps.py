
list1 = ['monday','tuesday','wednesday']

list2 = ['serial','movie','running']

dell = map(list1,list2)

def calculateSquare(n):
  return n*n

numbers = (1, 2, 3, 4)
result = map(calculateSquare, numbers)
print(result)

# converting map object to set
numbersSquare = set(result)
print(numbersSquare)