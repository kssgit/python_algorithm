def findMinIdx(ary):
    minIdx = 0
    for i in range(1,len(ary)):
        if (ary[minIdx] > ary[i]):
            minIdx = i
    return minIdx

before = [188,162,168,120,50,150,177,105]
after = []

for _ in range(len(before)):
    minPos = findMinIdx(before)
    after.append(before[minPos])
    del(before[minPos])

print(after)

testary = [124,33,44,55,22,52]
print('최솟 값-->', findMinIdx(testary))