def Decenterios(Pinakas):
    Metritakos = 0
    for i in range(len(Pinakas) - 1):
        if Pinakas[i] > Pinakas[i + 1]:
            Metritakos += 1
    return Metritakos


def Inverteridios(Pinakas):
    Metritakos = 0
    n = len(Pinakas)
    for i in range(n):
        for j in range(i + 1, n):
            if Pinakas[i] > Pinakas[j]:
                Metritakos += 1
    return Metritakos


if __name__ == "__main__":

    print("Dwse arithmous xwrismenous me keno:")
    user_input = input("> ")

    Pinakas = list(map(int, user_input.split()))

    print(f"\nYour Pinakasay: {Pinakas}")
    print(f"Arithmos Decents:   {Decenterios(Pinakas)}")
    print(f"Arithmos Inversions: {Inverteridios(Pinakas)}")