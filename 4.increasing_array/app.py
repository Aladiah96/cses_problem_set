def main():
    arr_len = int(input())
    arr = [int(s) for s in input().split()]
    total = 0

    if arr_len != len(arr):
        return

    for i in range(1, arr_len):
        diff = arr[i-1] - arr[i]
        if arr[i] < arr[i-1]:
            total += diff
            arr[i] = arr[i] + (diff)
    print(total)

if __name__ == "__main__":
    main()