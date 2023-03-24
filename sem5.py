"""def f(n):     
    if n == 0:         
        return   
    k = int(input())   
    f(n-1)    
    print(k, end=' ') 

n = int(input(""))
f(n)


def f(n): 
    if n == 0:
        return '' 
    k = int(input())  
    return f(n - 1) + f' {k}' 
                                #   return f(n-1) + ' ' + str(k) 
n = int(input())
print(f(n)[1:])

"""
from sem5_5 import *  
def all_square():     
    n = int(input("введите количество фигур: "))     
    s = 0     
    for num_fig in range(n):         
        plus_minus = input(" - или +: ")        
        symbol = 1         
        if plus_minus == "-":             
            symbol = -1         
        fig = input("введите фигуру(т, п, к): ")     
        if fig == "п":         
            n= int(input("введите ширину: "))   
            m= int(input("введите длину: "))   
            s+=symbol*rect(m,n)       
        elif fig == "т":          
            h= int(input("введите высоту: "))    
            m= int(input("введите основание: "))         
            s+=symbol*tri(m,h)         
        else:           
            r= int(input("ввдите радиус: "))    
            s+=symbol*circ(r)  
        return s 
print(all_square())