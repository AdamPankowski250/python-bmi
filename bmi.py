waga = float(input("Podaj wagę (kg):"))
wzrost = float(input("Podaj wzrost (m):"))

bmi = waga / (wzrost ** 2)

print("Twoje BMI wynosi:" , round(bmi, 2))

if bmi < 18.5:
    print("Niedowaga")
elif bmi < 25:
    print("Norma")
elif bmi < 30:
    print("Nadwaga")
else:
    print("Otyłość")
