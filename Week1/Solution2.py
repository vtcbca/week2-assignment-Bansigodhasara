#Write a python script to enter any number and print the sum of its digit.

def sumofdigit(num):
    A=num
    Ram=0
    Sum=0
    while(num!=0):
        Ram=num%10
        Sum=sum+Ram
        n//=10
    print(f"The sum of digit of number {A} is {Sum}!")  

num=int(input("Enter a number:"))
sumofdigit(num) 
