a = 7
b = 5

print(f"a = {a}, b = {b}\n")

comparisons = [
    ("a < b", a < b),
    ("a > b", a > b),
    ("a <= b", a <= b),
    ("a >= b", a >= b),
    ("a == b", a == b),
    ("a != b", a != b),
]

for expr, value in comparisons:
    print(f"{expr:8} -> {value}")

if a > b:
    print(f"\ndecisao: a ({a}) é maior que b ({b}).")
elif a < b:
    print(f"\ndecisao: a ({a}) é menor que b ({b}).")
else:
    print(f"\ndecisao: a ({a}) é igual a b ({b}).")