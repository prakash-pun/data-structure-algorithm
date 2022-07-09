def bubbleSort(dataSet):
    # start with the array length and decrement each time
    for i in range(len(dataSet) - 1, 0, -1):
        for j in range(i):
            if dataSet[j] > dataSet[j+1]:
                temp = dataSet[j]
                dataSet[j] = dataSet[j+1]
                dataSet[j+1] = temp
        print("Current State:", dataSet)


def main():
    list = [1, 20, 30, 4, 15, 28, 12, 43]
    bubbleSort(list)
    print("Result:", list)


if __name__ == "__main__":
    main()
