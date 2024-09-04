weight = input("What is your weight? ")

unit = input("(K)g or (L)bs: ")

lbs = float(weight) * 2.20462
kg = float(weight) / 2.20462

if unit.lower() == 'k':
    print("Weight in lbs: " + str(lbs))
elif unit.lower() == 'l':
    print("Weight in kg: " + str(kg))
else:
    print("Incorrect Input Type!")
