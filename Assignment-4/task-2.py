user_input = input("Enter some text to write to the file: ")
with open("output.txt", "w") as file:
    file.write(user_input + "\n") 
additional_data = "This line is appended to the file."
with open("output.txt", "a") as file:
    file.write(additional_data + "\n")
with open("output.txt", "r") as file:
    content = file.read()
print("\nFinal content of 'output.txt':")
print(content)
