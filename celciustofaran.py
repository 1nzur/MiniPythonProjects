x = input("Choose one of the following: \n" 
"1 to convert celsius into fahrenheit \n" 
"2 to convert fahrenheit into celsius : \n")
if x == "1":
    c = float(input("Enter the value of Celsius: "))
    f = (c * (9/5)) + 32
    print(f"{c}°C is equal to {f}°F")
elif x == "2":
    f = float(input("Enter the value of Fahrenheit: "))
    c = (f - 32) / 1.8
    print(f"{f}°F is equal to {c}°C")
else:
    print("Error: Invalid choice")

