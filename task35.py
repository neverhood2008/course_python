def check_number(n):
    if n==1:
        return "нет"
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return "нет"
    return "да"
print(check_number(int(input("число = "))))