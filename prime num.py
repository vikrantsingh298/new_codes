while True:
 num1=(input("Enter a number:"))
 
 
 if num1.isalpha()==True : 
      
      if num1 =='quit':    
            exit()

      print("Enter a number not character.....")       
     
 else:        
     c= int(num1)
     count=0
     for i in range(1,c+1):
          if c%i==0:
             count=count+1

     if count==2:
          print('The number is \'PRIME\'')


     else:
          print("\'NOT PRIME\'") 
 

