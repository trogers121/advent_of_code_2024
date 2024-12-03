if __name__ == '__main__':


    filename = '../../input.txt'
    # filename = '../../sample.txt'

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
        if all(r[i] <= r[i+1] for i in range(len(r) - 1)) or all(r[i] >= r[i+1] for i in range(len(r) - 1)):
            # r.sort()
            okay = True
            for l in range(len(r) - 1):
                diff = abs(r[l+1] - r[l])

                # print(diff)
                if diff >=1 and diff <= 3:
                    pass
                else:
                    okay = False
            # print(okay)
            if okay == True:
                safe_cnt += 1

        else:
            pass

    

    # print(report_list)
    print(safe_cnt)