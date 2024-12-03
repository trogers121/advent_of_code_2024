
def check_report(report: list[int]) -> int:
    '''
    -1 = Good
    All other indicate first bad index
    '''

    # Increasing?
    


if __name__ == '__main__':


    # filename = '../../input.txt'
    filename = '../../sample.txt'
    raise NotImplementedError

    report_list = []
    with open(filename, 'r') as f:
        while True:
            report = [int(x) for x in f.readline().split()]
            if report == []:
                break
            report_list.append(report)
    
    safe_cnt = 0
    for r in report_list[0:]:
        ## Check if the list is sorted

        r_copy = r
        bad_levels = 0 
        for i in range(len(r_copy) - 1):
            if r_copy[i+1] 

    

    # print(report_list)
    print(safe_cnt)