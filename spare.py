
while True:
 n=int(input())
 n1=0
 n2=1
 if n==0:
    print("Enter any number except zero...")

 elif n==1:
    print("0")    
 else:

  print(n1,end=" ")
  print(n2,end=" ")
  for i in range(2,n):
      summ=n1+n2
      print(summ,end=" ")
      n1,n2=n2,summ

