str_new="hgkeeeegkmgkdaaaaajjgjaaa  hhhhh hfjf nffhjjaae ".split()

#print(sum(map(str_new.count,"eyuioa")))
sum_1=[sum(map(elem.count,"eyuioa")) for elem in str_new]
print(sum_1)
print(sum(sum_1))