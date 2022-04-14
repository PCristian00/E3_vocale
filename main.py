def vocale(carattere):
    vocali = "aeiouAEIOU"

    if carattere in vocali:
        print(str(carattere)+" è una Vocale")
    else:
        print(str(carattere)+" NON è una Vocale")


car = input("Inserire un carattere: ");
vocale(car)
