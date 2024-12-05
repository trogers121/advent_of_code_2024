def is_first_four_rows(i):
    return (i < 4)
def is_first_four_columns(i):
    return (i < 4)
def is_last_four_rows(i):
    return (i < 4)
def is_last_four_columns(i):
    return (i < 4)

if __name__ == '__main__':
    
    filename = '../../input.txt'
    # filename = '../../sample.txt'

    with open(filename, 'r') as f:
        raw_lines = [x.strip().lower() for x in f.readlines()] # Remove newline characters
    
    
    # exit()

    word_to_find = 'mas'
    found_cnt = 0

    dims = (len(raw_lines)-1, len(raw_lines[0])-1)


    for row in range(1, len(raw_lines) - 1):
        # print(f"Row {row}: {[x for x in raw_lines[row]]}") # Show's how the first line is shown
        for col in range(len(raw_lines[0])):
            # Find the middle letter. Must be an A
            if raw_lines[row][col] != 'a':
                continue
            
            # Get the diagonals
            #  M M
            #   A
            #  S S
            try:
                bs_ = raw_lines[row - 1][col - 1] + raw_lines[row][col] + raw_lines[row + 1][col + 1]
                fs_ = raw_lines[row + 1][col - 1] + raw_lines[row][col] + raw_lines[row - 1][col + 1]
                
                # print(f"fs_={fs_} bs_={bs_}")
                if ((fs_ == 'mas') or (fs_ == 'sam')) and ((bs_ == 'mas') or (bs_ == 'sam')):
                    found_cnt += 1
            except:
                continue

            
        # print(f'Found: {found_cnt}')
            
    
    print(f"Found: {found_cnt}")

        

    