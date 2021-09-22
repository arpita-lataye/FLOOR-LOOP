n=int(input("enter the number:"))
for i in range (n):
    k=ord("a")+i
    for j in range(i+1):
        print(chr(k),end=" ")
        k=k+1
    print()