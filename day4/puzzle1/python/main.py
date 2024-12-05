if __name__ == '__main__':
    
    filename = '../../input.txt'
    # filename = '../../sample.txt'

    with open(filename, 'r') as f:
        raw_lines = [x.strip().lower() for x in f.readlines()] # Remove newline characters
    
    
    # exit()

    word_to_find = 'xmas'
    found_cnt = 0

    dims = (len(raw_lines)-1, len(raw_lines[0])-1)


    for row in range(len(raw_lines)):
        print(f"Row {row}: {[x for x in raw_lines[row]]}") # Show's how the first line is shown
        for col in range(len(raw_lines[0])):
            if raw_lines[row][col] != word_to_find[0]:
                continue

            # # Up-Left Diagonal
            if (row >= len(word_to_find)-1) and (col >= len(word_to_find)-1):
                word = ''
                for i in range(len(word_to_find)):
                    word += raw_lines[row - i][col - i]
                if word == word_to_find:
                    found_cnt += 1

            # # Up Line
            if (row >= len(word_to_find)-1):
                word = ''
                for i in range(len(word_to_find)):
                    word += raw_lines[row - i][col]
                if word == word_to_find:
                    found_cnt += 1

            # # Up - Right Diagonal
            if (row >= len(word_to_find)-1) and ((dims[1] - col) >= len(word_to_find)-1):
                word = ''
                for i in range(len(word_to_find)):
                    word += raw_lines[row - i][col + i]
                if word == word_to_find:
                    found_cnt += 1

            # # Left
            if (col >= len(word_to_find)-1):
                word = ''
                for i in range(len(word_to_find)):
                    word += raw_lines[row][col - i]
                if word == word_to_find:
                    found_cnt += 1
            
            # # Right
            if ((dims[1] - col) >= len(word_to_find)-1):
                word = ''
                for i in range(len(word_to_find)):
                    word += raw_lines[row][col + i]
                if word == word_to_find:
                    found_cnt += 1
            
            # # Down - Left Diagonal
            if ((dims[0] - row) >= len(word_to_find)-1) and (col >= len(word_to_find)-1):
                word = ''
                for i in range(len(word_to_find)):
                    word += raw_lines[row +i][col - i]
                if word == word_to_find:
                    found_cnt += 1
            
            # # Down
            if ((dims[0] - row) >= len(word_to_find)-1):
                word = ''
                for i in range(len(word_to_find)):
                    word += raw_lines[row + i][col]
                if word == word_to_find:
                    found_cnt += 1

            
            # # Down-Right Diagonal
            if ((dims[0] - row) >= len(word_to_find)-1) and ((dims[1] - col) >= len(word_to_find)-1):
                word = ''
                for i in range(len(word_to_find)):
                    word += raw_lines[row + i][col + i]
                if word == word_to_find:
                    found_cnt += 1
            
    
    print(f"Found: {found_cnt}")

        

    