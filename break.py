
# x=1
# while x<8:
#     x=x+1
#     if x==3:
#         continue
#     print(x)


a=[1,2,3,[2,3],4,7]
i=0
b=[]
while i<len(a):
    if type(a[i])!=list:
        b.append(a[i])
    i=i+1
print(b)

