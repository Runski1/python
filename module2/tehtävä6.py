import random
i = int(input("Kuinka monta numeroa haluat koodiisi? "))
a = int(input("Valitse pienin luku (0..9): "))
b = int(input("Valitse suurin luku (0..9): "))
x = 0
code = ""
while x < i:
    code += str(random.randint(a, b))
    x += 1
print(f"RNG-koodisi on: {code}")
