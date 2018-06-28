height = int(input("height: "))
weight = int(input("weight: "))
BMI = weight*10**4/height**2
print("BMI= ", BMI)
if BMI <16:
    print("severely underweight")
elif BMI < 18.5:
    print("underweight")
elif BMI <25:
    print("normal")
elif BMI <30:
    print("overweight")
else :
    print("obese")