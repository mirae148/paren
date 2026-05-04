def is_leap_year(year):
    """Возвращает True, если год високосный"""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def main():
    print("Добро пожаловать в Календарь-помощник!")
    while True:
        print("\nВыберите действие:")
        print("1. Проверить год на високосность")
        print("2. Узнать день недели по названию")
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
            print("(Функция 2 будет добавлена позже)")
        elif choice == "3":
            print("(Функция 3 будет добавлена позже)")
        elif choice == "4":
            print("(Функция 4 будет добавлена позже)")
        else:
            print("Неверный ввод, попробуйте снова")

if __name__ == "__main__":
    main()