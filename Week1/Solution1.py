# writer a program to print number ia a prime or not prime
N=int(input('enter any number:'))
Count=0
I=1
while I<=N:
    if(N%I==0):
        Count+=1
        I+=1
        if Count==2:
            print("prime number")
        else:
            print("not prime number")
