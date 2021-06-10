height = float(input("Enter your height in m:\n"))
weight = float(input("Enter your weight in kg:\n"))

bmi = round((weight/(height**2)))

print(f"Your BMI is {bmi}.")
if bmi <= 18.5:
    print("You are underweight. Eat more")
elif bmi > 18.5 and bmi <= 25:
    print("Your weight is normal. Keep up the good work")
elif bmi > 25 and bmi <= 30:
    print("You are overweight. Try reducing your calories intake and exercise to improve your health")
else:
    print("You are obese. Please consult your GP and start a plan to improve your health.")

