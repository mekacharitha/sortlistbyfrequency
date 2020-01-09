import functions
lis=[]
n=int(input("Enter the length of list "))
for i in range(n):
  lis1=list(input().split())
  lis.append(lis1)
lisort=functions.sorting(lis)
print(lisort)