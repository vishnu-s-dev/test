N=int(input())
arr1=list(map(int, input().split()))
arr2=list(map(int, input().split()))
D=int(input())

arr1.sort()
arr2.sort()
l=0
rev=arr2[::-1]
sum=0
for i in range(N):
    if (arr1[i]+rev[i] > D):
        sum=sum+arr1[i]+rev[i]
        l=l+1

s=(sum-(l*D))*100


print(s)
