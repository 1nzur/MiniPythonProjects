c="y"
while c=="y":
    grade = float(input("Enter the percentage"))
    if(100>=grade>90):
        print("A+")
    elif(grade>80):
        print("A")
    elif(grade>70):
        print("B+")
    elif(grade>60):
        print("B")
    elif(grade>50):
        print("C+")
    elif(grade>=40):
        print("C")
    elif(grade<40):
        print("F")
    else:
        print("Error")
    c = input("Do you want to enter grades of another student (y/n)")