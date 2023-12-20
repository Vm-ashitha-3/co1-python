list=[]
n=int(input("Enter the number of elements:"))
print("Enter",n,"values:")
for i in range(n):
    i=int(input())
    list.append(i)
print(list)
for i in list:
    if list[i]>100:
        list[i]="over"
print(list)
