import time
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

def Bubble(Pinakas):
    Pinakas = Pinakas.copy()
    n = len(Pinakas)
    MetrithsSygrisewn = 0

    for i in range(n):
        Fouskoma = False
        for j in range(0, n - i - 1):
            MetrithsSygrisewn += 1 
            if Pinakas[j] > Pinakas[j + 1]:
                Pinakas[j], Pinakas[j + 1] = Pinakas[j + 1], Pinakas[j]
                Fouskoma = True
        if not Fouskoma:
            break

    return Pinakas, MetrithsSygrisewn

def Insertion(Pinakas):
    Pinakas = Pinakas.copy()
    MetrithsSygrisewn = 0

    for i in range(1, len(Pinakas)):
        key = Pinakas[i]  # key to lene genika sthn python einai kati san to temp sthn C
        j = i - 1
        while j >= 0:
            MetrithsSygrisewn += 1            
            if Pinakas[j] > key:
                Pinakas[j + 1] = Pinakas[j]
                j -= 1
            else:
                break
        Pinakas[j + 1] = key

    return Pinakas, MetrithsSygrisewn

def MergeEpisodeITheSplit(Pinakas):  
    Pinakas = Pinakas.copy()
    MetrithsSygrisewn = [0]                               
    SortedPinakas = Helper_A_MergeStory(Pinakas, MetrithsSygrisewn)
    return SortedPinakas, MetrithsSygrisewn[0]

def Helper_A_MergeStory(Pinakas, MetrithsSygrisewn): #eftiaja mia trith synarthsh giati sthn C1 etsi opws ekana thn Episode 1 ousiastika kalei synexeia ton eayto ths kai midenizei to counter ousiastika kanei oti ekane h prwth prin kai h prwth apla kanei initbton metrith 
    if len(Pinakas) <= 1:
        return Pinakas
    mid = len(Pinakas) // 2
    left = Helper_A_MergeStory(Pinakas[:mid], MetrithsSygrisewn)
    right = Helper_A_MergeStory(Pinakas[mid:], MetrithsSygrisewn)
    return MergeEpisode2TheMergeStrikesBack(left, right, MetrithsSygrisewn)

def MergeEpisode2TheMergeStrikesBack(left, right, MetrithsSygrisewn):  # Ayto to meros kanei to merge
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        MetrithsSygrisewn[0] += 1                           
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def Roloi(SortFunc, Pinakas):
    start = time.perf_counter()
    SortedPinakas, MetrithsSygrisewn = SortFunc(Pinakas)
    end = time.perf_counter()
    Chronos = end - start
    return SortedPinakas, MetrithsSygrisewn, Chronos

MegethiPinaka = [100, 500, 1000, 2000, 5000]
Epanalipseis = 10

Algorithmoi = [
    ("Bublle Short" , Bubble),
    ("Insertion Short", Insertion),
    ("Merge Short", MergeEpisodeITheSplit),
]

Eisodoi = [
    ("Tajinomimenh", DimiourgeasI_Tajinomimenos),
    ("Anapodh", DimiuorgeasII_Anapodos),
    ("Tyxaia", DimiourgeasIII_Tyxaios),
    ("Ligotera Decents", DimiourgeasIV_OLigaDecents),
    ("Perissotera Decents",DimiourgeasV_OPollaDecents),
    ("Ligotera Inversions",DimiourgeasVI_OLigaInversions),
    ("Perissotera Inversions",DimiourgeasVII_OPollaInversions),
]

def PeiramatoTrexths():
    Apotelesmata = {}

    for OnomaAlgorithmou, LeitourgiaAlgorithmou in Algorithmoi:        
        Apotelesmata[OnomaAlgorithmou] = {}

        for OnomaEisodou, EidosEisodou in Eisodoi:                   
            Apotelesmata[OnomaAlgorithmou][OnomaEisodou] = {}

            for n in MegethiPinaka:                                    
                SynolikosChronos = 0
                SynolikesSygriseis = 0

                for _ in range(Epanalipseis):
                    Pinakas = EidosEisodou(n)
                    _, MetrithsSygrisewn, Chronos = Roloi(LeitourgiaAlgorithmou, Pinakas)
                    SynolikosChronos += Chronos
                    SynolikesSygriseis += MetrithsSygrisewn

                MesosChronos = SynolikosChronos / Epanalipseis
                MesesSygriseis = SynolikesSygriseis / Epanalipseis

                Apotelesmata[OnomaAlgorithmou][OnomaEisodou][n] = (MesosChronos, MesesSygriseis)
                print(f"{OnomaAlgorithmou:<20}{OnomaEisodou:<20}n={n:<6}")
                print(f"Mesos Chronos={MesosChronos:.6f}s  Meses Sygriseis={MesesSygriseis:.0f}")

    return Apotelesmata

if __name__ == "__main__":
    print(f"Sizes: {MegethiPinaka}")
    print(f"Repeats per experiment: {Epanalipseis}")

    Apotelesmata = PeiramatoTrexths()
    print("Done!")