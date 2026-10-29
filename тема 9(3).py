import math

a = float(input("Введіть першу сторону (a): "))
b = float(input("Введіть другу сторону (b): "))
angle_deg = float(input("Введіть кут між ними в градусах (gamma): "))

if a > 0 and b > 0 and 0 < angle_deg < 180:
    angle_rad = math.radians(angle_deg)

    c = math.sqrt(a**2 + b**2 - 2 * a * b * math.cos(angle_rad))

    if (a + b > c) or (a + c > b) or (b + c > a):
        perimeter = a + b + c

        print("\nТрикутник існує (перевірка суми сторін пройдена успішно).")
        print(f"Третя сторона (c): {c:.2f}")
        print(f"Перевірка: {a:.2f} + {b:.2f} > {c:.2f} -> {a + b > c}")
        print(f"Периметр трикутника: {perimeter:.2f}")
    else:
        print(
            "\nТрикутник не існує! Сума двох сторін має бути більшою за третю."
        )
else:
    print(
        "\nТрикутник не існує! Сторони мають бути більшими за 0, а кут у межах від 0 до 180 градусів."
    )