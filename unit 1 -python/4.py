num=int(input("enter N:"))
for i in range(1,11):
    print(f"{num}X{i}={num*i}")

n=int(input("enter N:"))
total=0
for i in range(1,n+1):
    total+=i
print(f"sum of first{n} numbers:{total}")
