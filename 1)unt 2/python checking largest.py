a=int(input("enter a"))
b=int(input("enter b"))
c=int(input("enter c"))
if(a>=b)and(a>=c):
    largest=a
    print(f"{a} is largest")
elif(b>=a)and(b>=c):
    largest=b
    print(f"{b} is largest")
else:
    largest=c
    print(f"{c} is largest")
