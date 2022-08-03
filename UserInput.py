# USER INPUT

while True:
    print("CREATE YOUR FIRST NAME AND LAST NAME")
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    name_confirmation = input(f"{first_name} {last_name}?\n")
    if name_confirmation == "no":
        continue
    elif name_confirmation == "yes":
        break
    else:
        print("INVALID! Please type 'yes' or 'no'.")
        quit()

print("CREATE YOUR USERNAME")
username = input("Username: ")
print(username + "@gmail.com")

while True:
    print("CREATE YOUR PASSWORD")
    password = input("Password: ")
    confirm_password = input("Confirm Password: ")
    if password == confirm_password:
        print("Account Successfully Created!")
        quit()
    else:
        continue
