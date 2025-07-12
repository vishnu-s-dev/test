N,D=map(int, input().split())
arr=list(map(int, input().split()))

sum=0
arr.sort()

for i in range(N-D,N):
    sum=sum+arr[i]
print(sum)
