import random

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

def DimiourgeasI_Tajinomimenos(n):
    return list(range(1, n + 1))

def DimiuorgeasII_Anapodos(n):
    return list(range(n, 0, -1))

def DimiourgeasIII_Tyxaios(n):
    Pinakas = list(range(1, n + 1))
    random.shuffle(Pinakas)
    return Pinakas

def DimiourgeasIV_OLigaDecents(n):
    k = max(1, n // 20)
    return DhmiourgeasDececntsOMegas(n, k)

def DimiourgeasV_OPollaDecents(n):
    k = min(n - 2, int((n - 1) * 0.95))
    return DhmiourgeasDececntsOMegas(n, k)

def DimiourgeasVI_OLigaInversions(n):
    max_inv = n * (n - 1) // 2
    k = max(1, max_inv // 20)
    return DhmiourgeasInversionsOPioMegas(n, k)

def DimiourgeasVII_OPollaInversions(n):
    max_inv = n * (n - 1) // 2
    k = int(max_inv * 0.95)
    return DhmiourgeasInversionsOPioMegas(n, k)

if __name__ == "__main__":

    n = 5
    print(f"Oi Dimiourgoi ftiaxnoun pinakes gia n ={n}\n")
    Dimiourgies = [
        ("Tajinomimenos",           DimiourgeasI_Tajinomimenos(n)),
        ("Anapodos",          DimiuorgeasII_Anapodos(n)),
        ("Tyxaios",           DimiourgeasIII_Tyxaios(n)),
        ("Ligotera descents",     DimiourgeasIV_OLigaDecents(n)),
        ("Perissotera descents",    DimiourgeasV_OPollaDecents(n)),
        ("Ligotera inversions",   DimiourgeasVI_OLigaInversions(n)),
        ("Perissotera inversions",  DimiourgeasVII_OPollaInversions(n)),
    ]

    for name, Pinakas in Dimiourgies:
        d = Decenterios(Pinakas)
        inv = Inverteridios(Pinakas)
        print(f"{name:<20} {str(Pinakas):<35} arithmos descents={d:<4} arithmos inversions={inv}")