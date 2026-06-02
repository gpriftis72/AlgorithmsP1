def DhmiourgeasDececntsOMegas(n, k):
    if k > n - 1:
        raise ValueError("Lathos! To k den mporei na jeperna to n-1 gia ta decents!")

    if k == 0:
        return list(range(1, n + 1))

    if k == n - 1:
        return list(range(n, 0, -1))

    Pinakas = list(range(1, n + 1))
    Pinakas[:k + 1] = Pinakas[:k + 1][::-1]
    return Pinakas


def DhmiourgeasInversionsOPioMegas(n, k):
    MegistaInversions = n * (n - 1) // 2
    if k > MegistaInversions:
        raise ValueError(f"Opa Lathos! To k den ginete na einai parapanw apo {MegistaInversions} gia n={n} dokimase pali!")

    contributions = []
    remaining = k
    for i in range(n - 1, -1, -1):
        c = min(remaining, i)
        contributions.append(c)
        remaining -= c
    contributions.reverse()

    result = []
    for i, c in enumerate(contributions):
        result.insert(len(result) - c, i + 1)
    return result

if __name__ == "__main__":

    print("\nDimiourgos gia Descents")

    n = int(input("Dwse to mhkos ths seiras (n): "))
    k = int(input(f"Posa Decents thes ? (apo 0 ews {n-1}): "))

    PinaksPrwtos = DhmiourgeasDececntsOMegas(n, k)
    print(f"\n O Pinakas sou :    {PinaksPrwtos}")
    print(f"Epivevaiwmena Decents :  {sum(1 for i in range(len(PinaksPrwtos)-1) if PinaksPrwtos[i] > PinaksPrwtos[i+1])}")

    MegistaInversions = n * (n - 1) // 2
    print("\n Dhmiourgos Inversions")

    n2 = int(input("Jana Dwse ena mhkos seiras :) (n): "))
    MegistaInversions2 = n2 * (n2 - 1) // 2
    k2 = int(input(f"Pes mou kai posa inversions thes  (apo 0 ews {MegistaInversions2}): "))

    PinaksDeyterosOJaderfosTouPrwtou = DhmiourgeasInversionsOPioMegas(n2, k2)
    print(f"\nO allos Pinakas sou:      {PinaksDeyterosOJaderfosTouPrwtou}")
    print(f"Exei epivevaiomanea {sum(1 for i in range(len(PinaksDeyterosOJaderfosTouPrwtou)) for j in range(i+1, len(PinaksDeyterosOJaderfosTouPrwtou)) if PinaksDeyterosOJaderfosTouPrwtou[i] > PinaksDeyterosOJaderfosTouPrwtou[j])} Inversions :")
