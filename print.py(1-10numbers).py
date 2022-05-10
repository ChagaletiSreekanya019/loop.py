# x=1
# while x<8:
#     print(x)
#     if (x==3):
#         break
#     x=x+1
a=int(input("enter the num"))
i=1
while i<=10:
    j=1
    while j<=a:
        print(j,"*",i,"=",j*i,  end="  ")
        j=j+1
    print()
    i=i+1

 