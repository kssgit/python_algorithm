
def selectionSort(ary):
    n = len(ary)
    # 전체 길이의 -1 만큼 사이클 반복
    for i in range(0,n-1):
        minIdx = i 
        # 첫번 째 값을 제외한 나머지에서 첫번째 값과 비교후 최소값 바꾸기
        for k in range(i+1,n):
            if ary[minIdx] > ary[k]:
                minIdx = k 
        tmp = ary[i]
        ary[i]=ary[minIdx]
        ary[minIdx]=tmp

    return ary


before = [188,162,168,120,50,150,177,105]

print('재 정렬-->',selectionSort(before) )