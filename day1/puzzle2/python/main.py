import math

if __name__ == '__main__':
    
    filename = '../../input.txt'
    # filename = '../../sample.txt'

    with open(filename, 'r') as f:
        raw_lines = f.readlines()

    list_a = []
    list_b = []
    for i in raw_lines:
        a = i.split()
        list_a.append(int(a[0]))
        list_b.append(int(a[1]))

    if len(list_a) != len(list_b):
        raise Exception("Lists are not equal length")

    similarity_score = 0
    for val in list_a:
        similarity_score += val * list_b.count(val)
    
    print(similarity_score)