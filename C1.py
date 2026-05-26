def Bubble(ThePinakasAndNumbers):
    ThePinakasAndNumbers = ThePinakasAndNumbers.copy()
    n = len(ThePinakasAndNumbers)
    for i in range(n):
        Fouskoma = False
        for j in range(0, n - i - 1):
            if ThePinakasAndNumbers[j] > ThePinakasAndNumbers[j + 1]:
                ThePinakasAndNumbers[j], ThePinakasAndNumbers[j + 1] = ThePinakasAndNumbers[j + 1], ThePinakasAndNumbers[j]
                Fouskoma = True
        if not Fouskoma: 
            break
    return ThePinakasAndNumbers

def Insertion(ThePinakasAndNumbers):
    ThePinakasAndNumbers = ThePinakasAndNumbers.copy()
    for i in range(1, len(ThePinakasAndNumbers)):
        key = ThePinakasAndNumbers[i] #key to lene genika sthn python einai kati san to temp sthn C
        j = i - 1
        while j >= 0 and ThePinakasAndNumbers[j] > key:
            ThePinakasAndNumbers[j + 1] = ThePinakasAndNumbers[j]
            j -= 1
        ThePinakasAndNumbers[j + 1] = key
    return ThePinakasAndNumbers

def MergeEpisodeITheSplit(ThePinakasAndNumbers): #thn espasa sta dyo giati thewritika o Mrge einai 2 diaforetikes leitourgies se mia opote gia ayto tous xwrisa
    ThePinakasAndNumbers = ThePinakasAndNumbers.copy()
    if len(ThePinakasAndNumbers) <= 1:
        return ThePinakasAndNumbers
    mid = len(ThePinakasAndNumbers) // 2
    left = MergeEpisodeITheSplit(ThePinakasAndNumbers[:mid])
    right = MergeEpisodeITheSplit(ThePinakasAndNumbers[mid:])
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
    ThePinakasAndNumbers = list(map(int, user_input.split()))

    print(f"\nO Pinakas pou edwses:{ThePinakasAndNumbers}")
    print(f"Sort me ton algorithmo Bubble:{Bubble(ThePinakasAndNumbers)}")
    print(f"Sort me Insertion: {Insertion(ThePinakasAndNumbers)}")
    print(f"Sort me Merge :{MergeEpisodeITheSplit(ThePinakasAndNumbers)}")