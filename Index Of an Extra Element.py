A = [2,4,6,8,9,10,12]
B = [2,4,6,8,10,12]
x=set(A)
y=set(B)
print(A.index((x-y).pop()))