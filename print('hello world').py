def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def get_weekday_name_ru(day_number):
    """Принимает номер дня недели (1=пн ... 7=вс) и возвращает название"""
    days = {
        1: "Понедельник",
        2: "Вторник",
        3: "Среда",
        4: "Четверг",
        5: "Пятница",
        6: "Суббота",
        7: "Воскресенье"
    }
    return days.get(day_number, "Неверный номер")

def main():
    print("Добро пожаловать в Календарь-помощник!")
    while True:
        print("\nВыберите действие:")
        print("1. Проверить год на високосность")
        print("2. Узнать день недели по номеру")
        print("3. Узнать количество дней в месяце")
        print("4. Создать заметку на день")
        print("5. Выйти")
        
        choice = input("Ваш выбор: ")
        
        if choice == "5":
            print("До свидания!")
            break
        elif choice == "1":
            year = int(input("Введите год: "))
            if is_leap_year(year):
                print(f"Год {year} — високосный (366 дней)")
            else:
                print(f"Год {year} — не високосный (365 дней)")
        elif choice == "2":
            num = int(input("Введите номер дня недели (1-7, где 1=пн, 7=вс): "))
            print(f"День: {get_weekday_name_ru(num)}")
        elif choice == "3":
            print("(Функция 3 будет добавлена позже)")
        elif choice == "4":
            print("(Функция 4 будет добавлена позже)")
        else:
            print("Неверный ввод, попробуйте снова")

if __name__ == "__main__":
    main()