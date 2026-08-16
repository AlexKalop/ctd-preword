name=(input("What is your name? "))
print("Hello "+ name + "!")
age=int((input("How old are you? ")))

if (age>3 and age<=11):
    print(name+", you are a child and your ticket price is $12")
elif (age>13 and age<=64):
    print(name+", you are a adult and your ticket price is $15")
elif (age>65):
    print(name+ ", you are an senior and your ticket price is $12")
else:
        print(name+ ", your admission is Free!")
        
        
## This is a short program to calculate the price of admission to the zoo based of age. The program asks the user for their name and then their age. Checks to see if its a kid, adult, senior or free if under the age of 3.