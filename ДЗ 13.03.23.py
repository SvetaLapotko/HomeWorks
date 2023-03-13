s = input("Знак (+,-,*,/): ")
a = int(input("a="))
b = int(input("b="))

if s == '+':
    print((a + b))
elif s == '-':
    print((a - b))
elif s == '*':
    print((a * b))
elif s == '/':
    if b != 0:
        print((a / b))
    else:
        print("Деление на ноль!")
