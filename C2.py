import time

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

if __name__ == "__main__":

    print("Dwse arithmous xwrismenous me keno gia na tous kanw Sort:")
    user_input = input("> ")
    Pinakas = list(map(int, user_input.split()))

    print(f"\nO Pinakas pou edwses: {Pinakas}")

    for name, func in [("Sort me ton Algorithmo Bubble ",    Bubble),
                       ("Sort me Insertion", Insertion),
                       ("Sort me Merge",     MergeEpisodeITheSplit)]:
        SortedPinakas, MetrithsSygrisewn, Chronos = Roloi(func, Pinakas)
        print(f"{name:<20} {str(SortedPinakas):<25} {MetrithsSygrisewn:<15} Xronos Ektelesis: {Chronos:.6f}") #to evala .6f giati synithos kinitai se ayta ta epipeda , pio poluy kai tha eixe parapanw leptomeria , axreiasth
        