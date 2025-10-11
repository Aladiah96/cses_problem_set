def process(n, arr):
    arr.sort()

    if n not in arr:
        return n

    for num, index in enumerate(arr):
        if index - num > 1:
            return num+1

def main():
    # file_path = "./tests/13.in"
    #
    # try:
    #     with open(file_path, 'r') as f:
    #         lines = f.readlines()
    #         n = int(lines[0])
    #         n_arr = [int(s) for s in lines[1].split()]
    #         pass
    # except FileNotFoundError:
    #     print(f"FileNotFoundError")

    n = int(input())
    n_arr = [int(s) for s in input().split()]
    result = process(n, n_arr)
    print(result)

if __name__ == "__main__":
    main()
