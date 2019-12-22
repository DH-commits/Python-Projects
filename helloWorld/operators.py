for i in range(1, 5):
    print(i)

#for i in range(1.4, 5):
   # print(i) #in range cannot use float so throws an error

    #Expressions, anything that can be calculated to return a value

animal = 'parrot'
print(animal)
print(animal[3]) #indexed at 0, prints (2nd) r of parrot


#Negative indexes, basically a mirror
print(animal[-1]) #prints t, as t is the -1, o is -2, r is -3 etc

#SLICING

animal = 'Norwegian Blue bird'
print(animal[0:5]) #prints from index:0 to index:4, 5 is not included, so its -1, output will be norwe
print(animal[0:9]) #starts at index 0 and extends up to but not including 9
print(animal[5:10]) #starts at index 5 and goes to up to but not including index position 10
print(animal[:10]) #didnt provide a start value but defaults to 0th index

computerParts = ['monitor', 'harddrive', 'mouse'];
print(computerParts[1]) # prints harddrive
print(computerParts[1][2]) # prints the second index of the first index in the array. so letter r of hardware

#range is an example of a sequence that cant be multiplied
