print('example single quotes', "python double quotes") #single or double quotes doesnt matter, just be consistent
print('hi')
print("hello")
print("hello" + " world") #concatenation

greeting = "hello"

name = input('enter name: ') #text stored in name variable, input function called

print(greeting + " " + name) #variable concatenation

#return value of input function is assigned to name variable. dynamic typed, don't need to declare var type

print(greeting + " " + input('enter name: ')) #calling function within function

#the escape character, eg. \n (new line) \t (new tab)
splitString = 'This string\n has been\n split' #escape characters coloured different
print(splitString)

tabbedString = 'one\t two\t three\t four'
print(tabbedString)

anotherSplitString = """This string has been
split into several
different lines"""
print(anotherSplitString)
print("C:\tom\notes") #thinks theres a tab and a new line escape character
#to work around this, use double \\ or regular expression: r"
print('C:\\tom\\notes')
print(r'C:\tom\notes')



