MAXIMUM_TIMES = 10;
for i in range(1, MAXIMUM_TIMES):
    print('i is: {0}'.format(i))

number = '9,2304,304930,4039'
#for i in range(0, len(number)):
 #   print(number[i])


for i in range(0, len(number)):
    if number[i] in '012345':
        print(number[i])

cleanedNumber = ''
for char in number:
    if char in '012345':
        cleanedNumber = cleanedNumber + char;
        print(cleanedNumber)

for i in range(0, 100, 5):
    print(i, end='') #prints out in steps of 5
    print('i is: {0}'.format(i))
                     #overwriting the end parameter to print onto the same line
