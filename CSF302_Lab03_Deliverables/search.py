import random

def binary_search(arr, key):
    low, high = 0, len(arr) - 1
    comparisons = 0
    while low <= high:
        mid = (low + high) // 2
        comparisons += 1
        if arr[mid] == key:
            return mid, comparisons
        if key < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1, comparisons

def ternary_search(arr, key):
    low, high = 0, len(arr) - 1
    comparisons = 0
    while low <= high:
        third = (high - low) // 3
        mid1 = low + third
        mid2 = high - third

        comparisons += 1
        if arr[mid1] == key:
            return mid1, comparisons

        comparisons += 1
        if arr[mid2] == key:
            return mid2, comparisons

        if key < arr[mid1]:
            high = mid1 - 1
        elif key > arr[mid2]:
            low = mid2 + 1
        else:
            low, high = mid1 + 1, mid2 - 1

    return -1, comparisons

def make_array(n):
    # Unique sorted values make present/absent tests easy.
    return sorted(random.sample(range(1, max(10*n, 20) + 1), n))

def menu():
    arr = []
    while True:
        print("\n1. Generate sorted random array")
        print("2. Display array")
        print("3. Binary Search")
        print("4. Ternary Search")
        print("5. Best-case step count")
        print("6. Worst-case step count")
        print("7. Comparison table")
        print("8. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            n = int(input("Enter n: "))
            arr = make_array(n)
            print("Array generated.")
        elif choice == "2":
            print(arr)
        elif choice in ("3", "4"):
            if not arr:
                print("Generate an array first.")
                continue
            key = int(input("Enter key: "))
            result = binary_search(arr, key) if choice == "3" else ternary_search(arr, key)
            print("Index:", result[0], "Comparisons:", result[1])
        elif choice == "5":
            if not arr:
                print("Generate an array first.")
                continue
            key = arr[len(arr)//2]
            print("Best case:")
            print("Binary:", binary_search(arr, key)[1], "comparison(s)")
            print("Ternary:", ternary_search(arr, key)[1], "comparison(s)")
        elif choice == "6":
            if not arr:
                print("Generate an array first.")
                continue
            key = -1  # absent, so the search reaches its termination
            print("Worst/absent case:")
            print("Binary:", binary_search(arr, key)[1], "comparison(s)")
            print("Ternary:", ternary_search(arr, key)[1], "comparison(s)")
        elif choice == "7":
            print("n | Binary worst | Ternary worst")
            for n in [8, 16, 32, 64, 128, 256, 512, 1024]:
                a = make_array(n)
                b = binary_search(a, -1)[1]
                t = ternary_search(a, -1)[1]
                print(f"{n:4} | {b:12} | {t:13}")
        elif choice == "8":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    menu()
# Analysis / Conclusion:
#The binary search technique will cut the search space in half approximately every step:
# T(n) = T(n/2) + O(1) = O(log n).
#In the case of a ternary search, the range is narrowed down to approximately ⅓
# T(n) = T(n/3) + O(1) = O(log n).
#The two therefore are asymptotically logarithmic.
#The number of comparisons is impacted by the fact that ternary
#The two middle positions in each iteration are checked during # search. Therefore, even
#They're both O(log n), but the two are not the same when compared in terms of counts.