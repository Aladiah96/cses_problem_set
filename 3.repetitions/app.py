def count_repetitions(str):
    count = 1
    max_count = 1

    for i in range(1, len(str)):
        if str[i] == str[i-1]:
            count += 1
        else:
            max_count = max(max_count, count)
            count = 1

    return max(max_count, count)

def main():
    str = input()
    result = count_repetitions(str)
    print(result)       

if __name__ == "__main__":
    main()