#Write a program to calculate the area of a a circle.
"""radius=eval(input("Enter the radius of the circle:"))
area=3.14*radius*radius
print("The area of the circle is:",area)"""

#Check whether a number is even or odd.
"""number=float(input("Input a number:"))
if number%2==0:
    print("The number is even.")
else:
    print("The number is odd.")
"""

#Find factorial using recursion.
"""def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
num=int(input("Enter a number to find its factorial:"))
print("The factorial of",num,"is",fact(num))"""

#Count vowels and consonants in a string.
countv=0
countc=0
string=input("Enter a string:")
for char in string:
    if char in "aeiouAEIOU":
        countv+=1
    else:
        if char.isalpha():
            countc+=1
print("The number of vowels in the string is:",countv)
print("The number of consonants in the string is:",countc)


#Print fibonacci series up to n terms.
nterms = int(input("Enter the number of terms: "))
n1, n2 = 0, 1
count = 0
# check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")
# if there is only one term, return n1
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,"is:")
   print(n1)
# generate fibonacci sequence
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1