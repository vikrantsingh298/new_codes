str1=(input("Enter any String:"))
alnum=0
alpha=0
digit=0
lower=0
upper=0
for i in range(0,len(str1)):
    if str1[i].isalnum()==True: alnum+=1
    if str1[i].isalpha()==True: alpha+=1
    if str1[i].isdigit()==True: digit+=1
    if str1[i].islower()==True: lower+=1
    if str1[i].isupper()==True: upper+=1

print("True") if alnum!=0 else print("False")
print("True") if alpha!=0 else print("False")
print("True") if digit!=0 else print("False")
print("True") if lower!=0 else print("False")
print("True") if upper!=0 else print("False")


        
        
        
        
             

