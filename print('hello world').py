def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def get_weekday_name_ru(day_number):
    days = {1: "Пн", 2: "Вт", 3: "Ср", 4: "Чт", 5: "Пт", 6: "Сб", 7: "Вс"}
    return days.get(day_number, "?")  # краткие названия для списка

def days_in_month(month, year=2000):
    if month < 1 or month > 12:
        return "Неверный месяц"
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 2 and is_leap_year(year):
        return 29
    return month_days[month - 1]

# Функция 4: работа с заметками
notes = []  # глобальный список заметок, каждая заметка = {"date": "2026-05-04", "text": "..."}

def add_note(date, text):
    notes.append({"date": date, "text": text})
    print(f"Заметка на {date} добавлена!")

def filter_notes_by_date(keyword):
    """Фильтрует заметки по части даты (например, '2026-05')"""
    filtered = [note for note in notes if keyword in note["date"]]
    return filtered

def main():
    global notes
    print("📅 Календарь с заметками TATARIN2010")
    while True:
        print("\nМеню:")
        print("1. Проверить високосный год")
        print("2. Название дня недели")
        print("3. Дней в месяце")
        print("4. Добавить заметку на день")
        print("5. Показать все заметки и фильтровать")
        print("6. Выйти")
        
        choice = input("Выбор: ")
        
        if choice == "6":
            break
        elif choice == "1":
            y = int(input("Год: "))
            print("Високосный" if is_leap_year(y) else "Нет")
        elif choice == "2":
            n = int(input("Номер дня (1-7): "))
            print(get_weekday_name_ru(n))
        elif choice == "3":
            m = int(input("Месяц (1-12): "))
            y = int(input("Год: "))
            print(f"{days_in_month(m, y)} дней")
        elif choice == "4":
            date = input("Дата (ГГГГ-ММ-ДД): ")
            text = input("Текст заметки: ")
            add_note(date, text)
        elif choice == "5":
            if not notes:
                print("Нет заметок. Сначала добавьте.")
                continue
            print("\nВсе заметки:")
            for i, note in enumerate(notes, 1):
                print(f"{i}. {note['date']}: {note['text']}")
            filt = input("Введите фильтр по дате (Enter - пропустить): ")
            if filt:
                filtered = filter_notes_by_date(filt)
                print(f"\n📌 Отфильтровано по '{filt}':")
                for note in filtered:
                    print(f"{note['date']}: {note['text']}")
        else:
            print("Неверно")

if __name__ == "__main__":
    main()