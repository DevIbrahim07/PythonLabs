length_cm = float(input("Enter a length in centimeters: "))

if length_cm < 0:
    print("The entry is invalid")
else:
    length_inches = length_cm / 2.54
    print(f"{length_cm} centimeters is {length_inches} inches")
