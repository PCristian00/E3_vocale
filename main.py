def vocale(carattere):
    vocali="aeiou"

    if carattere in vocali:
        print("Vocale")
    else:
        print("Non Vocale")

car=input("Inserire un carattere: ");
vocale(car)