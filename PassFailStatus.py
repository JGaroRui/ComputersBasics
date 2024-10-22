tc=int(input("Tell me the total number of classes\n> ")) # Ask for the variables
ac=int(input("Tell me the classes that the student attended\n> "))
es=float(input("Tell me the exam score that the student achieve\n> "))
def percent_of_attendance(tc,ac): # Define a function that calculates the coefficient of attendance
    return ac/tc
if percent_of_attendance(tc,ac)<0.8: # Check the conditions to pass the subject
    print("He failed the subject")
else:
    if es<70:
        print("He failed the subject")
    else:
        print("He pass the subject")

