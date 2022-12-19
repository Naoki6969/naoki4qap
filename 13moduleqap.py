n = int(input("Введите колличество билетов необходимых на мероприятие:\n"))
if n <= 0:
    raise ValueError("Указано неверное значение колличества билетов")
price = 0
for i in range(n):
    age = int(input(f"Уточните возраст посетителя № {i+1}:\n"))
    if age < 18:
        price += 0
    if 18 <= age < 25:
        price += 990
    if age >= 25:
        price += 1390
    else:
        raise ValueError("Указано неверное значение возраста посетителя")
if n >= 3:
    price = int(price * 0.9)  # 90% цена билета со скидкой

print("Ваша цена с учётом скидок будет", price, "руб")
