a=int(input("enter 3 values"))
b=int(input())
c=int(input())
if(a>b and a>c):
    print(a,"is largest")
else:
    if(b>c):
        print(b,"is largest")
    else:
        print(c,"is largest")
