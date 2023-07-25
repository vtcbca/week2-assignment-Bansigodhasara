# program to check palindrom number
N=int(input("Enter a number to be checked:"))
Reverse=0
C=N
while(N!=0):
    Remainder=N%10
    Reverse=Reverse*10+Remainder
    N//=10
if C==Reverse:
    print(f"{C} is a palindrome number")
else:
    print(f"{C} is not a palindrome number")
