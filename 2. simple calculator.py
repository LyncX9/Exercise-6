def kalkulator(angka1, angka2, operator):
    if operator == "+":
        return angka1 + angka2
    elif operator == "-":
        return angka1 - angka2
    elif operator == "*":
        return angka1 * angka2
    elif operator == "/":
        if angka2 == 0:
            return "Error: Pembagian dengan 0 tidak diizinkan"
        else:
            return angka1 / angka2
    else:
        return "Error: Operator tidak valid"

angka1 = float(input("Enter First Number: "))
angka2 = float(input("Enter Second Number: "))
operator = input("Input Operator (+, -, *, /): ")

hasil = kalkulator(angka1, angka2, operator)
print("Hasil:", hasil)