from random import randint
def checkValue(myarray,mini,maxi):
    return [elem for i,elem in enumerate(myarray) if mini<=elem<=maxi]
arrlen=int(input(  ))
mearr=[randint(0,10) for _  in range(arrlen)]
print(*mearr)
print(checkValue(mearr,0,5))