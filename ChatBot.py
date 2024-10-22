n=str(input("Hello, tell me your name\n> ")) # Ask for the variables
y=int(input(f"Okay, {n} now tell me the year you were born\n> ")) 
m=int(input("Tell me the month\n> "))
d=int(input("Tell me the day\n> "))

def age(y): # Define a function that calculate your age
    return 2024-y

print(f"{n} you are {age(y)} years old")
h=str(input("Tell me your favorite hobbie\n> "))
print(f"So, you're {n} you are {age(y)} and your hobbie is {h} and your birthday is {d} of {m}") # Print the results