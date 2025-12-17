username = "User"
password = "Password"
entered_username = input("Enter your username: ")
entered_password = input("Enter your password: ")

if entered_username == username and entered_password == password:
        print(f"Welcome {username}")
else:
    print("Incorrect username or password (2 attempts left)")
    for attempt in range(2):
        if attempt == 0:
            entered_usernametry1 = input("Enter your username: ")
            entered_passwordtry1 = input("Enter your password: ")
            if entered_usernametry1 == username and entered_passwordtry1 == password:
                print(f"Welcome {username}")
            else:
                print("Incorrect username or password (1 attempts left)")
        elif attempt == 1:
            entered_username = input("Enter your username: ")
            entered_password = input("Enter your password: ")
            if entered_username == username and entered_password == password:
                print(f"Welcome {username}")
            else:
                print("You ran out of attempts")
