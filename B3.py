def Decenterios(arr):
    Metritakos = 0
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            Metritakos += 1
    return Metritakos


def Inverteridios(arr):
    Metritakos = 0
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                Metritakos += 1
    return Metritakos


if __name__ == "__main__":

    print("Dwse arithmous xwrismenous me keno:")
    user_input = input("> ")

    arr = list(map(int, user_input.split()))

    print(f"\nYour array: {arr}")
    print(f"Arithmos Decents:   {Decenterios(arr)}")
    print(f"Arithmos Inversions: {Inverteridios(arr)}")