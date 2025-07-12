n=int(input("num"))
arr=[] 
for i in range(n):
    arr.append(int(input()))
sum1=0
maxsum=float('-inf')
for i in range(n):
    sum1=sum1+arr[i]

    if sum1> maxsum:
        maxsum=sum1

    if sum1 < 0 :
        sum1=0   
    
    

print(maxsum)
       
       
   
