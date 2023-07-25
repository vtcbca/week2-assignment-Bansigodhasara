# program to check whether number is armstrong number or not
Num=int(input("Enter a number to be checked:"))
Result=0
C=Num
for I in range(Num):
     if Num!=0:
         R=Num%10
         Result+=R*R*R
         Num//=10
if Result==C:
     print(f"{C} is a armstrong number")
else:
    print(f"{C} is not a armstrong number")
