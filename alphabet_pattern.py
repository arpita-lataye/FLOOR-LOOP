n=int(input("enter the number:"))
k=ord("A")
# for i in range (n):
#     for j in range(i+1):
#         print(chr(k),end=" ")
#         k=k+1
#     print()

i=1
while i<=n:
    j=1
    while j<=(i+1):
        print(chr(k),end=" ")
        k=k+1
    print()