from random import randint
def fillArray(arraySize):
    array=[]
    for i in range(arraySize):
        num=randint(0,10)
        array.append(num)
    return array
def uniq(array1,array2):
    for i in range(lenArray1):
        if array1[i] not in array2:
            print(array1[i], end= " ")
lenArray1=int(input("введите количество элементов в первом массиве = "))
lenArray2=int(input("введите количество элементов в втором массиве = "))
myArray1=fillArray(lenArray1)
myArray2=fillArray(lenArray2)
print(myArray1)
print(myArray2)
uniq(myArray1,myArray2)