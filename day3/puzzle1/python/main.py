import re

if __name__ == '__main__':
   
    # filename = '../../input.txt'
    filename = '../../sample.txt'

    with open(filename, 'r') as f:
        memory = f.read()

    
    # Do a regex operation on memory to find all instances of mul
    mul_ops:list[str] = re.findall("mul\([0-9]{1,3},[0-9]{1,3}\)", memory)

    # print(mul_ops)

    mul_sum = 0
    for op in mul_ops:
        vals = [int(x) for x in op.removeprefix('mul(').removesuffix(')').split(',')]
        mul_sum += vals[0] * vals[1]

    print(mul_sum)