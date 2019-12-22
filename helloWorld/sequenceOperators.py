#interestingly you can * sequence types like strings

string1 = 'Im '
string2 = "watching "
string3 = "Silicon "
string4 = "Valley "

print(string1 + string2 + string3 + string4) # Typical + operator in a sequence type
print(string1 * 5) # Multiplication operator in a sequence type. Prints Im Im Im Im Im

age = 24;
week = 7;

# print("my age is " + age + " years old") # wont work as cant concatenate int in string
print("my age is {0} years old".format(age)) # so to coerce the int to a string we can do this
print("my age is {0} years old and there are {1} days in this week".format(age, week))

for i in range(1,20):
    print('{0} squared is {1}'.format(i, i**2))


print(f"Age is {age}") #python 3.6 introducted f-strings, similar to replacement strings but cleaner!