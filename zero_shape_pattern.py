
for row in range(6):
    for col in range(5):
        if ((row==0 or row==5) and 0<col<4) or ((col==0 or col==4 )and 0<row<5):
            print('*',end=" ")
        else:
            print(end="  ")
    print()   

# for row in range(5):
#     for col in range(4):
#         if (row==1 ) or (col==0 or col==3):
#             print('*',end=' ')
#         else:
#             print(end="  ")
#     print()


# for row in range(4):
#     for col in range(5):
#         if (row==1) or (col==0 or col==4 or col==1) or (col==2 and row==2 ):
#             print('*',end=' ')
#         else:
#             print(end="  ")
#     print()