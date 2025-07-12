n=int(input())
arr1=list(map(int, input().split()))
arr2=list(map(int, input().split()))
arr1.sort()
arr2.sort()

rev=arr2[::-1]
sum=0
for i in range(n):
    sum=sum+(arr1[i]*rev[i])
print(sum)
