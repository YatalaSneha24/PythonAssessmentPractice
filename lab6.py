#Inserting space between outputs using commas
print("The sum of 5 and 2 is", 5+2)
print("The product of 5 and 2 is", 5*2)

#Custom seperator between outputs
print("5", "+", "3", "=", 5 + 3, sep=" ")
print("4", "*", "7", "=", 4*7, sep="*")

#Inserting text at the end of a print statement using end parameter
print("5+3=", end="")
print(5+3)
print("5 * 2 = ",end="")
print(5*2)