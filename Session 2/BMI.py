height_in_cm = input("How tall are you in centimeters?")
height_in_m = int(height_in_cm)/100
weight_in_kg = input("How heavy are you in kilograms?")
BMI=height_in_m/int(weight_in_kg)
if BMI <16:
    print("Severely underweight")
elif BMI < 18.5:
    print ("Underweight")
elif BMI < 25:
    print("Normal")
elif BMI<30:
    print("Overweight")
else:
    print("Obese")
