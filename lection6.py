"""list=[1,2,3,4,5,7]
list2=[]
for i in range(len(list)):
    if list[i]%2==0:
        a=list[i]
        list2.append((a,a*a))
print(list2)

def select(f, col):
    return [f(x) for x in col]
def where(f, col):
    return [x for x in col if f(x)]
data = [1, 2, 3, 5, 8, 15, 23, 38]
print(data)
print(type(data[0]))
res=data
#res = select(int, data)
#print("select")
#print(res)
res = where(lambda x: x % 2 == 0, res)
print("where")
print(res) # [2, 8, 38]
res = list(select(lambda x: (x, x ** 2), res))
print (res)
"""

list_1 = [x for x in range (1,20)]
print(list_1)
list_1 = map(lambda x: x + 10, list_1 )
print(list_1)
list_1 = list(map(lambda x: x + 10, list_1 ))
print(list_1)