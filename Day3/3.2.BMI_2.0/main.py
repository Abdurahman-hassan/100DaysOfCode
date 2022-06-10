height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = round(float(weight) / float(height ** 2))

if bmi < 19:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif 19 < bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif 25 < bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif 30 < bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")
elif bmi > 35:
    print(f"Your BMI is {bmi}, you are clinically obese.")
