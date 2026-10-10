#Temperature Converter: Convert Celsius ↔ Fahrenheit using functions
def cels_fahren(celsius):
    fahrenheit=(celsius*9/5)+32
    return fahrenheit
def fahren_cels(fahrenheit):
    celsius=(fahrenheit-32)*5/9
    return celsius
print("Temperature Converter:")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
choice = int(input("Enter your choice (1 or 2): "))
if choice == 1:
    celsius = float(input("Enter temperature in Celsius: "))
    print("Temperature in Fahrenheit:", cels_fahren(celsius))
elif choice == 2:
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    print("Temperature in Celsius:", fahren_cels(fahrenheit))
else:
    print("Invalid choice!")

#Student Grade Calculator: Take marks as input, calculate average & assign grades
def calculate_grade(marks):
    average=sum(marks)/len(marks)
    if average >=90:
        return "A"
    elif average >=80:
        return "B"
    elif average>=70:
        return "C"
    elif average>=60:
        return "D"
    else:
        return "Fail"
marks=list(map(float, input("Enter marks for 5 subjects: ").split()))
print("Grade:", calculate_grade(marks))

#Even/Odd & Prime Number Checker.
num=int(input("Enter a number:"))
if num%2==0:
    print("The number is even.")
else:
    print("The number is odd.")
is_prime=True
if num>1:
    for i in range(2,num):
        if num%i==0:
            is_prime=False
            break
    if is_prime:
        print("The number",num,"is a prime number.")
    else:
        print("The number",num,"is not a prime number.")
