''' Python Primitive Data Types
String
Integer -
Float - 
Boolean
'''
my_string = ("This is a string")
print(type(my_string))
print(my_string[3]) #3rd caracter starting from 0
print(my_string[-1]) #last caracter

my_number = 1_750_320 # use "_" as convention to legibility 
print(type(my_number))
print(my_number)

my_float_number = 3.141592
print(type(my_float_number))
print(my_float_number)


my_boolean = True
my_boolean = False #changing the value
print(type(my_boolean))
print(my_boolean)

print("My age: " + str(26)) #Type conversion

number = 2.7
print(int(number)) #is rounded down when converting



''' Mathematical Operations 
PEMDAS hierarchy:
P - parentesis 
E - exponents &
M - multiplications 
D - divitions &
A - addition
S - subtraction
Reading from left to the right (L->R)
'''
print(10 + 25)
print(10 - 25)
print(10 * 25)
print(51 / 25) #implicit tuype castint (converting the result into a float)
print(51 // 25) #round down the number no matter the decimal number
print(3 ** 3)


''' Excercise 4: BMI Calculator
The body mass index (BMI) is a measure used in medicine to see if someone is 
underweight or overweight. This is the formula used to calculate it:
BMI is equal to the person's weight divided by the person's height squared
'''
height = 1.75
weight = 65.5
bmi = (weight / (height ** 2))

print("Your bmi is: " + str(bmi))
print(f"Your rounded bmi with again with a f-string is: {round(bmi, 2)}") #2 digits

