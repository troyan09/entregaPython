import random
words = ["python", "programación", "computadora", "código", "desarrollo",
         "inteligencia"]
secret_word = random.choice(words)
max_attempts = 10
guessed_letters = []
print("¡Bienvenido al juego de adivinanzas!")
print("Estoy pensando en una palabra. ¿Puedes adivinar cuál es?")
word_displayed = "_" * len(secret_word)
print(f"Palabra: {word_displayed}")

for i in range(max_attempts):
    letter = input("Ingresa una letra: ").lower()
    if letter != "":
        if letter in guessed_letters:
            print("Ya has intentado con esa letra. Intenta con otra.")
            continue
        guessed_letters.append(letter)
        if letter in secret_word:
            print("¡Bien hecho! La letra está en la palabra.")
        else:
            print("Lo siento, la letra no está en la palabra.")
            letters = []
            for letter in secret_word:
                if letter in guessed_letters:
                    letters.append(letter)
                else:
                    letters.append("_")
            word_displayed = "".join(letters)
            print(f"Palabra: {word_displayed}")

            if word_displayed == secret_word:
                print(f"Felicidades, has adivinado la palabra secreta")
                break
    else:
        print("Error! ingrese solo letras")
else:
    print(f"¡Oh no! Has agotado tus {max_attempts} intentos.")
    print(f"La palabra secreta era: {secret_word}")
