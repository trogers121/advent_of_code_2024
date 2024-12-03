import re

if __name__ == '__main__':
   
    filename = '../../input.txt'
    # filename = '../../sample2.txt'

    with open(filename, 'r') as f:
        memory = f.read()


    # First find all do() and don't()s
    idx = 0
    enabled = True
    working_mem = memory
    enabled_memory = ""

    dont_str = "don't()"
    do_str = 'do()'
    search_str = dont_str
    while(True):
        try:
            # print(working_mem)
            slice_idx = working_mem.index(search_str)
            # print(f'Slice_idx = {slice_idx}')
            if enabled:
                enabled = False
                search_str = do_str
                enabled_memory += working_mem[:slice_idx]
            else:
                enabled = True
                search_str = dont_str
            # Strip working mem and repeat.
            working_mem = working_mem[slice_idx:]
        except ValueError:
            # print("error")
            # No more don't() instructions. Slice to end of string and place in enabled_memory_string
            if enabled:
                enabled_memory += working_mem
            break


    # print(enabled_memory)
    # Do a regex operation on memory to find all instances of mul
    mul_ops:list[str] = re.findall("mul\([0-9]{1,3},[0-9]{1,3}\)", enabled_memory)

    # print(mul_ops)

    mul_sum = 0
    for op in mul_ops:
        vals = [int(x) for x in op.removeprefix('mul(').removesuffix(')').split(',')]
        mul_sum += vals[0] * vals[1]

    print(mul_sum)