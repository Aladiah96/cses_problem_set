def is_even(num):
    return num % 2 == 0

def process(num):
    num_arr = [num]

    while num > 1:
        if is_even(num):
            num = num/2
        else:
            num = (num * 3) + 1
        num_arr.append(int(num))

    return num_arr

def main():
    num = int(input())

    print(" ".join(map(str, process(num))))

if __name__ == "__main__":
    main()
