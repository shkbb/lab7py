import random

def guess_game():
    print("Вгадай, кого або що я загадав. Це може бути щось живе, неживе або вигадане.")
    secret = random.choice(["кіт", "камінь", "єдиноріг"])
    hints = {
        "кіт": "Це має лапи та вуса.",
        "камінь": "Це важке і не рухається.",
        "єдиноріг": "Це існує лише у фантазіях."
    }

    attempts = 0
    max_attempts = random.randint(4, 6)
    
    while attempts < max_attempts:
        guess = input("Ваша здогадка: ").strip().lower()
        
        if not guess:
            print("Введення не може бути порожнім. Спробуйте ще.")
            continue
        
        attempts += 1

        if guess == secret:
            print("Ви вгадали! Це дійсно", secret + "!")
            return
        elif attempts == 2:
            print("Підказка:", hints[secret])
        else:
            print("Не вгадали. Спробуйте ще.")

    print(f"Ви не вгадали. Це було: {secret}.")

if __name__ == "__main__":
    guess_game()
