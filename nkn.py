def count_Triplets(A, N):
     count = 0
     A.sort()
     for i in range(N-2):
       c=(A[i] + A[i+1]+ A[i+2])/3
       d=(A[i] + A[i+1]+ A[i+2])//3
       if c-d==0:
         count+=1
 
     return count

a=list(map(int,input().split()))   
print(count_Triplets(a,len(a)))  
