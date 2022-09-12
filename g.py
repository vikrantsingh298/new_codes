b=input()
A=list(map(int,b.split()))
N=len(A)
count = 0
for i in range(N-2):
  c=(A[i] + A[i+1]+ A[i+2])/3
  d=(A[i] + A[i+1]+ A[i+2])//3
  if c-d==0:
    count+=1
    print(count)
        
        