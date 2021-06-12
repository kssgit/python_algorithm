# 신규 아이디 추천
# 내 문제 풀이
def solution(new_id):
    answer = ''
    #소문자 치환
    new_id_1 = new_id.lower()
    # 해당 문자열 말고 제거
    new_id_2 =''
    for s in new_id_1:
        if s.islower() or (s in ['-','_','.']) or s.isdigit() :
            new_id_2+=s
    # .가 2번 이상 연속된 부분 하나로 치환
    new_id_3 = ''
    for i in range(len(new_id_2)):
        if i>0:
            if  new_id_2[i] =='.':
                if new_id_2[i] != new_id_2[i-1]:
                    new_id_3 += new_id_2[i] 
            else:
                new_id_3 += new_id_2[i] 
        else:
            new_id_3 += new_id_2[i]          
    #4단계
    new_id_4 = ''
    for i in range(len(new_id_3)):
        if i == 0 or i == len(new_id_3)-1:
            if new_id_3[i] != '.':
                new_id_4 +=new_id_3[i]
        else:
            new_id_4 +=new_id_3[i]
    #5단계
    if new_id_4 =='':
        new_id_4 +='a'
    #6단계
    new_id_5 = new_id_4
    if len(new_id_4) >=16:
        new_id_5 = new_id_4[:15]
   
   
    if new_id_5[len(new_id_5)-1] =='.':
        new_id_5 = new_id_5[:len(new_id_5)-1]
    # 7 단계
  
    if len(new_id_5)<=2:
        a = new_id_5[len(new_id_5)-1]
        while len(new_id_5)<3:
      
            new_id_5+=a
    answer = new_id_5
    return answer

# 다른 사람 문제 풀이
import re

def solution2(new_id):
    st = new_id
    st = st.lower()
    st = re.sub('[^a-z0-9\-_.]', '', st)
    st = re.sub('\.+', '.', st)
    st = re.sub('^[.]|[.]$', '', st)
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    return st


new_id ="...!@BaT#*..y.abcdefghijklm"
answer = solution(new_id)
print(answer)
result = "bat.y.abcdefghi"