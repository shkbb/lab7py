import random
import time

def is_valid_input(user_input):
    return user_input.replace(" ", "").isalpha()

def get_random_hint(hints_given, all_hints):
    available = [hint for i, hint in enumerate(all_hints) if i not in hints_given]
    if available:
        chosen = random.choice(available)
        index = all_hints.index(chosen)
        hints_given.add(index)
        return chosen
    return None

def game():
    entities = [
        {
            "answer": "шарік",
            "famous": False,
            "hints": [
                "Це ім’я може бути у пса.",
                "Це персонаж із мультфільму.",
                "Він не людина.",
                "Іноді його вважають героєм, але не всі його знають."
            ]
        },
        {
            "answer": "альберт ейнштейн",
            "famous": True,
            "hints": [
                "Його ім’я пов’язане з фізикою.",
                "Він дуже відомий, але не поп-зірка.",
                "Має шалену зачіску.",
                "Його прізвище стало символом геніальності."
            ]
        },
        {
            "answer": "гаррі поттер",
            "famous": True,
            "hints": [
                "Цей герой має шрам.",
                "Він ходив до школи, якої не існує.",
                "Його друг — рудий.",
                "Його боїться темна істота."
            ]
        }
    ]

    selected = random.choice(entities)
    answer = selected["answer"]
    hints = selected["hints"]
    hints_given = set()

    print("Спробуйте вгадати: це відома людина чи ні?")
    attempts = 0

    while True:
        user_input = input("Ваш варіант або 'підказка': ").strip().lower()
        
        if user_input == "підказка":
            hint = get_random_hint(hints_given, hints)
            if hint:
                print("Підказка:", hint)
            else:
                print("Більше підказок немає.")
            continue
        
        if not is_valid_input(user_input):
            print("Схоже, ви ввели щось дивне. Введіть ім’я або запитайте підказку.")
            continue

        attempts += 1

        if user_input == answer:
            time.sleep(random.uniform(0.5, 2))
            if selected["famous"]:
                print("Ви вгадали! Це справді була відома особа:", answer.title())
            else:
                print("Це було щось не дуже відоме... Але ви вгадали.")
            return
        else:
            if random.random() < 0.3:
                print("Можливо, ви близько...")
            else:
                print("Ні, це не те.")

        if attempts >= 5 and random.random() < 0.4:
            print("Гра несподівано завершена. Правильна відповідь була:", answer.title())
            return

if __name__ == "__main__":
    game()
