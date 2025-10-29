#Single-quoted strings
single_quoted = 'Konnichiwa, Sneha'

#String operations with single-quoted strings
upper_case = single_quoted.upper()
print("Uppercase version:", upper_case)
length = len(single_quoted)
print("Length of the string:", length)
lower_case = single_quoted.lower()
print("Lowercase version:", lower_case)
contains_substring = 'Sneha' in single_quoted
print("Contains 'Sneha':", contains_substring)

#Replacing Strings
single='Arigato, Sneha'
chandu_string = single.replace("Sneha", "Elephant")
print(chandu_string)
#Printing words in the string
words=single.split()
print(words)