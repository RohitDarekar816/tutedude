# Write a program to create a text file and write some content to it.

with open('output.txt', 'w') as file:
    file.write("Hello, World!\n")

with open('output.txt', 'r') as file:
    (print(file.read()))
