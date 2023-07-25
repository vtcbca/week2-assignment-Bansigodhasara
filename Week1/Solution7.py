#7.Write a python script to enter any string, replace vowel with its position number.

def vowelchange(s):
    B=''
    A=('a','e','I','o',u'','A','E','I','O','U')
    for index,j in enumerate(S):
        if(j in A):
            B+=str(index)
        else:
            B+=j

    print(f"The string '{S}' after change is '{B}' ")

S=input("Enter a string:")
vowelchange(S)
