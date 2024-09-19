#Question 1:Currency Converter

# convert currency Rupees to Dollar
print("Convert rupees into dollars:")
rupeesAmount = int(input("Enter the amount in Rs.:"))
rsintodollar = (rupeesAmount/84)
print(rupeesAmount,"convert into dollar" , rsintodollar)
# Convert Dollar to Rupees
print("Convert dollars into rupees:")
dollarAmount = int(input("Enter the amount in $.:"))
dollarintors = (dollarAmount*84)
print(dollarAmount,"convert into rupees",dollarintors);


#Question 2:BMI Calculator

# asking for input from the users  
the_height = float(input("Enter the height in cm: "))  
the_weight = float(input("Enter the weight in kg: "))  
# defining a function for BMI  
the_BMI = the_weight / (the_height/100)**2  
# printing the BMI  
print("Your Body Mass Index is", the_BMI)  
# using the if-elif-else conditions  
if the_BMI <= 18.5:  
    print("Oops! You are underweight.")  
elif the_BMI <= 24.9:  
    print("Awesome! You are healthy.")  
elif the_BMI <= 29.9:  
    the_print("Eee! You are over weight.")  
else:  
    print("Seesh! You are obese.")



#Question 3:Age Year calculator
    
#Taking input from the user
born_year = int(input("Enter born year: "))
current_year = int(input("Enter current year: "))
age = current_year - born_year
print("My Age is", age)                       
    





