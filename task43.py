array1 = [int(i) for i in input().split()]

print(array1)
count = 0
for i in range(len(array1)-1):
    for j in range(i+1,len(array1)-1):
        if array1[i] == array1[j] and array1[i+1]==array1[j+1]:
            count += 1

print(count)