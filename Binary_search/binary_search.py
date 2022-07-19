def welcome():
    global array,entre
    array = []
    x = -1
    while x < 99:
        x += 2
        array.append(x)
        continue

    # print(right, left, mid)
    entre = str(input("Please enter a value\n"))
    binary_search()


def binary_search():
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = str(((left + right) / 2))
        if array[mid] == entre:
            return mid
            break
        elif entre < array[mid]:
            right = mid - 1
            continue
        elif entre > array[mid]:
            left = mid + 1
            continue
        else:
            print("The number is not in this")
            break

def main():
    welcome()

if __name__ == '__main__':
    main()
