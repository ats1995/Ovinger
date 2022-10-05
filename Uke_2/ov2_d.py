userAge = float(input("User age: "))

if userAge < 0:
    print("Age cannot be negative.")
elif userAge < 4:
    print("Gratis")
elif userAge >= 4 and userAge <= 16:
    print("45 kroner")
elif userAge >= 17 and userAge <= 66:
    student = input("Student (Ja/Nei): ")
    if student == "Ja":
        print("50 kroner")
    elif student == "Nei":
        print("90 kroner")
elif userAge >= 67:
    print("50 kroner")