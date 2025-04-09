import random
import time

def get_fake_or_real_hint(answer, hints_real, hints_fake):
    # Іноді правильна підказка, іноді — фальшива
    if random.choice([True, False]):
        return random.choice(hints_real.get(answer, []))
    else:
        return random.choice(hints_fake)

def end_game_with_mystery(answer, guessed_correctly):
    time.sleep(1)
    if guessed_correctly and random.random() < 0.5:
        print("Можливо, ви справді щось зрозуміли.")
    elif guessed_correctly:
        print("Чи це справді була правильна відповідь?..")
    else:
        print("Можливо, ви не туди дивились.")
    print("Гру завершено.")

def game():
    # Список доступних категорій (гравцю не повідомляється, що він має вибрати саме з них)
    valid_categories = {
        "число": "42",
        "колір": "зелений",
        "вигадане слово": "кроблін"
    }

    hints_real = {
        "42": ["Це відповідь, але ви не знаєте на яке питання.", "Має дві цифри.", "Більше ніж 30, менше ніж 50."],
        "зелений": ["Цей колір має трава.", "Зустрічається на світлофорі.", "Має букв більше ніж 'синій'."],
        "кроблін": ["Це слово не знайдете у словнику.", "Звучить вигадано.", "Ніхто його не використовує."]
    }

    hints_fake = [
        "Це пов'язано з кішками.", "Його носив Наполеон.", "Це має запах буряка.",
        "З цим пов’язано число Пі.", "Воно було у кожного у 90-х."
    ]

    print("Виберіть, що ви хочете вгадати: щось... будь-що. Але не все підходить.")

    choice = input("Що ви хочете вгадати? ").strip().lower()

    if choice not in valid_categories:
        print("Це не те, що ви можете вгадати. Але гра продовжується.")
        answer = random.choice(list(valid_categories.values()))
    else:
        answer = valid_categories[choice]

    print("Почнемо. Ви можете писати відповіді або просити 'підказку'. Але не все має сенс.")

    attempts = 0
    max_attempts = random.randint(4, 8)
    guessed = False

    while attempts < max_attempts:
        user_input = input("Ваш варіант: ").strip().lower()

        if not user_input:
            print("Мовчання — теж відповідь. Але не допоможе.")
            continue

        if user_input == "підказка":
            hint = get_fake_or_real_hint(answer, hints_real, hints_fake)
            print("Підказка:", hint)
            continue

        attempts += 1

        if user_input == answer:
            guessed = True
            break
        else:
            responses = [
                "Можливо, ви близько.",
                "Це не зовсім те.",
                "Варіант цікавий, але ні.",
                "Таке ми вже бачили, і що з того?"
            ]
            print(random.choice(responses))

    end_game_with_mystery(answer, guessed)

if __name__ == "__main__":
    game()
