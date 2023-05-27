def calculator():
    num1 = float(input("Введите первое число: "))
    operator = input("Введите оператор (+,-,*,/): ")
    num2 = float(input("Введите второе число: "))

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 == 0:
            print("Ошибка: Деление на ноль")
            return
        else:
            result = num1 / num2
    else:
        print("Ошибка: Недопустимый оператор")
        return

    print(f"Результат: {result}")

calculator()
