import random
words = ["python", "programación", "computadora", "código", "desarrollo",
         "inteligencia"]
secret_word = random.choice(words)
max_error = 5

guessed_letters = []
print("¡Bienvenido al juego de adivinanzas!")
print("Estoy pensando en una palabra. ¿Puedes adivinar cuál es?")
word_displayed = "_" * len(secret_word)
print(f"Palabra: {word_displayed}")
vocales = ["a", "e", "i", "o", "u"]
# voit me permite añladirle a guessed_letters las vovales para que cuenten como letras ya ingresadas y se impriman aunque falle
voit = []


def modo_deficil():
    cant_error = 0
    while cant_error < max_error:
        letter = input("Ingresa una letra: ").lower()
        if letter != "":
            if letter in guessed_letters:
                print("Ya has intentado con esa letra. Intenta con otra.")
                cant_error += 1
                continue
            guessed_letters.append(letter)
            if letter in secret_word:
                print("¡Bien hecho! La letra está en la palabra.")
            else:
                print("Lo siento, la letra no está en la palabra.")
                cant_error += 1
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
        print(f"¡Oh no! Has agotado tus {max_error} intentos.")
        print(f"La palabra secreta era: {secret_word}")


def modo_medio():
    cant_error = 0
    guessed_letters.append(secret_word[0])
    guessed_letters.append(secret_word[-1])
    letters = []
    for letter in secret_word:
        if letter in guessed_letters:
            letters.append(letter)
        else:
            letters.append("_")
    word_displayed = "".join(letters)
    print(f" Palabra:{word_displayed}")
    while cant_error < max_error:
        letter = input("Ingresa una letra: ").lower()
        if letter != "":
            if letter in guessed_letters:
                print("Ya has intentado con esa letra. Intenta con otra.")
                cant_error += 1
                continue
            guessed_letters.append(letter)
            if letter in secret_word:
                print("¡Bien hecho! La letra está en la palabra.")
            else:
                print("Lo siento, la letra no está en la palabra.")
                cant_error += 1
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
        print(f"¡Oh no! Has agotado tus {max_error} intentos.")
        print(f"La palabra secreta era: {secret_word}")


def modo_facil():
    cant_error = 0
    guessed_letters = voit + vocales
    letters = []
    for letter in secret_word:
        if letter in guessed_letters:
            letters.append(letter)
        else:
            letters.append("_")
    word_displayed = "".join(letters)
    print(f" Palabra:{word_displayed}")
    while cant_error < max_error:
        letter = input("Ingresa una letra: ").lower()
        if letter != "":
            if letter in guessed_letters:
                print("Ya has intentado con esa letra. Intenta con otra.")
                cant_error += 1
                continue
            guessed_letters.append(letter)
            if letter in secret_word:
                print("¡Bien hecho! La letra está en la palabra.")
            else:
                print("Lo siento, la letra no está en la palabra.")
                cant_error += 1
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
        print(f"¡Oh no! Has agotado tus {max_error} intentos.")
        print(f"La palabra secreta era: {secret_word}")


options = int(input("""Ingrese que dificultad quieres:
                         [1] Facil 
                         [2] Media 
                         [3] Dificil 
                         """))
match options:
    case 3:
        modo_deficil()
    case 2:
        modo_medio()
    case 1:
        modo_facil()
