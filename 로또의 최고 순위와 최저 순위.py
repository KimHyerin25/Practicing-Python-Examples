def solution(lottos, win_nums):
    rank = [6,6,5,4,3,2,1]
    cnt = 0
    zero = 0

    for num in lottos:
        if num == 0:
            zero +=1
            continue

        for win in win_nums:
            if num == win:
                cnt +=1

    high = rank[zero + cnt]
    low = rank[cnt]

    return [high, low]