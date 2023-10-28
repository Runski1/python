num1 = float(input("Anna leiviskät: "))
num2 = float(input("Anna naulat: "))
num3 = float(input("Anna luodit: "))
num4 = num1 * 20 * 32 * 13.3 + num2 * 32 * 13.3 + num3 * 13.3
kg = num4 // 1000
g = num4 - kg * 1000
print(f"Massa nykymittojen mukaan \n"
      f"{kg} kilogrammaa ja {g:.2f} grammaa.")
