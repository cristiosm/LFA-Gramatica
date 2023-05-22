def impartire_gramatica(fisier):
    gramatica = {}

    with open(fisier, "r") as f:
        for linie in f:
            stanga, dreapta = linie.strip().split("->")
            stanga = stanga.strip()
            dreapta = dreapta.strip().split("|")
            gramatica[stanga] = [simbol.strip() for simbol in dreapta]

    return gramatica


def acceptare(gramatica, simbol_s, cuvant):
    if cuvant == "":
        if 'lambda' in gramatica[simbol_s]:
            return True
        else:
            return False

    for tranzitie in gramatica[simbol_s]:
        if tranzitie[0] == cuvant[0]:
            restul_cuvant = cuvant[1:]
            if acceptare(gramatica, tranzitie[1], restul_cuvant):
                return True
        elif len(tranzitie) == 1 and tranzitie == cuvant[0]:
            return True

    return False


simbol_s = 'S'
gramatica = impartire_gramatica("gramatica.in")
cuvinte = "cuvinte.in"

with open(cuvinte, "r") as f:
    for linie in f:
        cuvant = linie.strip()
        if acceptare(gramatica, simbol_s, cuvant):
            print(f"Cuvantul '{cuvant}' este generat de gramatica.")
        else:
            print(f"Cuvantul '{cuvant}' nu este generat de gramatica.")
