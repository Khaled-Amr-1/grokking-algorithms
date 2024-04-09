def main():
    item = input("Enter the item : ")
    data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(binary_search(data, int(item)))


def binary_search(data, item):
    low = 0
    high = len(data) - 1

    while low <= high:
        mid = (low + high) // 2
        if item == mid:
            return mid
        elif item > mid:
            low = mid + 1
        elif item < mid:
            high = mid - 1
        else:
            return None


main()
