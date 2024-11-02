#Opening files('r is read' 'w is write')
with open("login_attempts.txt", "r") as file:
    file_text = file.read()
print(file_text)
