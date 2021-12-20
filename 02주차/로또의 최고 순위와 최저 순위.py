# 망한 내 답
def solution(lottos, win_nums):
    answer = []
    if lottos.count(0) = 0:
        answer = [1,1]
    if lottos.count(0) = 1:
        answer = [1,2]
    if lottos.count(0) = 2:
        answer = [3,5]
    if lottos.count(0) = 3:
        answer = [4,4]
    if lottos.count(0) = 4:
        answer = [3,5]
    if lottos.count(0) = 5:
        answer = [1,6]
    if lottos.count(0) = 6:
        answer = [1,6]
        
    return answer

# 예시답안
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