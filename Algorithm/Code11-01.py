def findMinIdx(ary):
    minIdx = 0
    for i in range(1,len(ary)):
        if (ary[minIdx] > ary[i]):
            minIdx = i
    return ary[minIdx]


testary = [124,33,44,55,22,52]
print('최솟 값-->', findMinIdx(testary))