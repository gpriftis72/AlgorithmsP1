def Bubble(Pinakas):
    Pinakas = Pinakas.copy()
    n = len(Pinakas)
    for i in range(n):
        Fouskoma = False
        for j in range(0, n - i - 1):
            if Pinakas[j] > Pinakas[j + 1]:
                Pinakas[j], Pinakas[j + 1] = Pinakas[j + 1], Pinakas[j]
                Fouskoma = True
        if not Fouskoma: 
            break
    return Pinakas

def Insertion(Pinakas):
    Pinakas = Pinakas.copy()
    for i in range(1, len(Pinakas)):
        key = Pinakas[i] #key to lene genika sthn python einai kati san to temp sthn C
        j = i - 1
        while j >= 0 and Pinakas[j] > key:
            Pinakas[j + 1] = Pinakas[j]
            j -= 1
        Pinakas[j + 1] = key
    return Pinakas

def MergeEpisodeITheSplit(Pinakas): #thn espasa sta dyo giati thewritika o Mrge einai 2 diaforetikes leitourgies se mia opote gia ayto tous xwrisa
    Pinakas = Pinakas.copy()
    if len(Pinakas) <= 1:
        return Pinakas
    mid = len(Pinakas) // 2
    left = MergeEpisodeITheSplit(Pinakas[:mid])
    right = MergeEpisodeITheSplit(Pinakas[mid:])
    return MergeEpisode2TheMergeStrikesBack(left, right)

def MergeEpisode2TheMergeStrikesBack(left, right): #Ayto to meros kanei to merge 
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

if __name__ == "__main__":

    print("Dwse arithmous xwrsimenous me keno gia na tou kanw Sort:")
    user_input = input("> ")
    Pinakas = list(map(int, user_input.split()))

    print(f"\nO Pinakas pou edwses:{Pinakas}")
    print(f"Sort me ton algorithmo Bubble:{Bubble(Pinakas)}")
    print(f"Sort me Insertion: {Insertion(Pinakas)}")
    print(f"Sort me Merge :{MergeEpisodeITheSplit(Pinakas)}")