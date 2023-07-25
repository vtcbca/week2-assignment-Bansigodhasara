#5.Write a python script to enter any string and count vowel.

def vowels(S):
    A=('a','e','I','o','u','A','E','I','O','U')
    vowel=0
    for I in S:
        if I in A:
            Vowel+=1
    print(f"The vowels count in '{S}' is {vowel}")

S=input("Enter a string:")
vowels(S)
