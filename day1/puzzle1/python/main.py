import math

if __name__ == '__main__':
    
    filename = '../input.txt'
    # filename = '../sample.txt'

    with open(filename, 'r') as f:
        raw_lines = f.readlines()

    list_a = []
    list_b = []
    for i in raw_lines:
        a = i.split()
        list_a.append(int(a[0]))
        list_b.append(int(a[1]))
    # print(list_a)
    # print(list_b)

    list_a.sort()
    list_b.sort()

    if len(list_a) != len(list_b):
        raise Exception("Lists are not equal length")

    # print(list_a)
    # print(list_b)
    diff_sum = 0
    for i in range(len(list_a)):
        diff_sum += abs(list_a[i] - list_b[i])
    
    print(diff_sum)