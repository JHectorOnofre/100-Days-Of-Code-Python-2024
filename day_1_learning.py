#Printing to the console in Python
print("Hello Python")


#String manipulation and Code Intelligence
print("hello world \nHello Python \nThis is day one")

print("My name is: " + "Hector") #concatenation


#The Python input function
print("Hello " + input("what is your name? "))


#Python Variables 
favorite_color = input("And which is your favorite color ? ")
print("Woa, " + favorite_color +" is a very nice color! :D")

pet_name = input("Which is a cute pet name? ")
print(f"great, that name has {len(pet_name)} letters")


'''CODE EXCERCISE: Variables
We have 2 variables glass1 and glass2. glass1 contains milk and glass2 contains juice. 
Write 3 lines of code to switch the contents of the variables. You are not allowed to 
type the words "milk" or "juice". You are only allowed to use variables to solve this 
exercise.'''

glass1 = "milk"
glass2 = "juice"
print("The glass 1 conatins " + glass1)
print("The glass 2 conatins " + glass2)

glass3 = glass1
glass1 = glass2
glass2 = glass3
print("The glass 1 now conatins " + glass1)
print("The glass 2 now conatins " + glass2)


#Variable Naming (make the code readable)
 
