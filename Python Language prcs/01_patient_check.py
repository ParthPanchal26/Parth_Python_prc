# print("------------------------------------")

patientName = input("\nWhat is your name? ")
patientAge = input("What is your age? ")
isSick = input("Are your suffering any illness? Yes or No! ")
# Here all variables holds sting data!

patientName = patientName.lower()
isSick = isSick.lower()

if patientName == "john smith":
    if isSick == "yes":
        print("\nPatient Name: ", patientName)
        print("Patient Age: ", int(patientAge))
        '''
        Here we have type-casted variable from string to integer
        Some example of built-in typecasting functions are
        int(), float(), bool(), str() 
        '''
else:
    print("\nNo record found!")
