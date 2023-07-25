#6.Write a python script to enter any string and print only part of string. Take input of start character and end character from user.


def partstring(S):
    St=int(input("Enter start position:"))
    E=int(input("Enter end position:"))

    print(f"The part of the string '{S}' is '{S[St-1:E:]}'")

S=input("Enter a string:")
partstring(S) 
