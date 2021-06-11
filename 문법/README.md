#  파이썬 문법



## 연산

```python
#나누기
17/3
>>>5.66666

## 목 구하기 (//)
17//3 
>>> 5

##나머지 구하기
17%3
>>>2

#제곱
5**2
>>>25

#소수점 반올림 round(float,표시할 소수점 자리수)
round(3.1415151515 , 2)
>>> 3.14
```



## 수학 함수 math



~~~ python
import math

#제곱근 
math.sqrt(25)
>>>5

#로그함수
math.log2(10)
>>>3.3219280

##다른 math 함수를 알고 싶다
print(help(math))
~~~





## 문자열

### 기본 문자열 문법

``` python
#문자열 안에 ' 표시하기
print('I dont\'t know')
print('say "I don\'t konw"')
print("say \"I don't konw\"")

# 줄 바꿈
print('hello. \nHow ard you?')
# row 데이타 표시
print(r'C:\name\name')
>>> C:\name\name
    
# 공백 문자 없애기
print("""\
line1
line2
line3\
""")
>>>
lin1
lin2
lin3

# 문자열,리테랄? 연속
print('py''thon') 또는 print('py'+'thon')
>>>python
##단 변수안에 있는 문자열일 경우 +
```



### 문자열의 인덱스와 슬라이스

```python
word = 'python'
## 제일 마지막 문자열 출력
print(word[-1])
>>>n

## slice 
print(word[0:2]) == print(word[:2])
>>>py
print(word[2:5])
>>>tho

## 문자열의 값 변경 ** 문자열은 대입 연산이 않된다** word[0]='j'  XX
word = 'j'+word[1:]
print(word)
>>>jython

```



### 문자 메소드

``` python
s = 'My name is Mike. Hi Mike'
##해당 문자열이 있는지 확인 startswith('문자열') boolean
s.startswith('My')
print(s)
>>>True
s.startswith('X')
print(s)
>>>False

##해당 문자열의 위치 find('문자열') int
print(s.find('Mike'))
>>>11
### 뒤에서부터 찾아라
print(s.rfind('Mike'))
>>>20

## 몇개가 있냐 coubt('Mike')
print(s.count('Mike'))
>>>2

## 첫문자만 대문자 나머지 소문자 capitalize
s.capitalize()
>>>My name is mike. hi mike


## 각 단어의 첫 문자 대문자 title()
s.title()
>>>My Name Is Mike. Hi Mike


## 모든 문자 대문자로 upper()
## 모든 문자 소문자 lower()
## 문자열 대체 replace(원래문자,대체문자)
print(s.replace('Mike','Nancy'))
>>>My Name Is Nancy. Hi Nancy


```



### 문자의 대입

 ```python
 'a is {}'.format('a')
 >>>'a is a'
 'a is {}'.format('test')
 >>>'a is test'
 'a is {} {} {}'.format(1,2,3)
 >>>'a is 1 2 3'
 'a is {0} {1} {2}'.format(1,2,3)
 >>>'a is 1 2 3'
 'a is {2} {1} {0}'.format(1,2,3)
 >>>'a is 3 2 1'
 ## format 변수 지정 가능
 'My name is {family} {name}. 나의 이름은 {name} {family}'.format(name ='kim', family='seong soo')
 
 ## f-string
 name ='kim'
 family='seong soo'
 print(f'My name is {family} {name}. 나의 이름은 {name} {family}')
 
 ```



## 데이타 구조

### 리스트

```python

l = [1,2,3,4,5,6,7,8,9,10]

# 리스트 전체 출력
print(l[:])

#문자열 리스트 변형
list('abcdefg')
>>>['a', 'b', 'c', 'd', 'e', 'f', 'g']

# 한번씩 건너 띄어서 출력
l[::2]
>>>[1,3,5,7,9]

# 뒤에서부터 거꾸로 출력
l[::-1]
>>[10,9,8,7,6,5,4,3,2,1]

## 2차원 배열
a = ['a','b','c']
n=[1,2,3,4]
x = [a,n]
print(x)
>>> [['a','b','c'],[1,2,3,4]]
```



### 리스트 조작

```python
#리스트는 값 변경 가능
s = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
s[0]='X'
>>>['X', 'b', 'c', 'd', 'e', 'f', 'g']

## 특정 범위의 값 변경
s[2:5] = ['C','D','E']
print(s)
>>>['X','b','C','D','E','f','g']

##특정 범위의 값 지우기
s[2:5] =[]
print(s)
>>>['X','b','f','g']


n = [1,2,3,4,5,6,7,8,9,10]
# 리스트 추가 append(추가할 값)
n.append(100)
>>>[1,2,3,4,5,6,7,8,9,10,100]

#특정 위치에 값 추가 insert(index, 값 )

# 제일 뒤에 있는 값 추출 및 제거 pop()

# 값 제거 del -- 주의해서 사용하자
del n[0]
>>>[2,3,4,5,6,7,8,9,10,100]

## 제일 처음만나는 값 제거 remove(값)
n = [1,2,2,3]
n.remove(2)
print(n)
>>>[1,2,3]

#리스트에 리스트 추가 + , += 말고 extend()
x = [1,2,3,4,5]
y = [6,7,8,9,10]
x.extend(y)
print(X)
>>> [1,2,3,4,5,6,7,8,9,10]
```



### 리스트의 메소드

```python
r = [1,2,3,4,5,1,2,3]
#제일 처음만나는 값의 index 출력  index(값, index의 뒤에서부터)
print(r.index(3))
>>>2
print(r.index(3,3))
>>>7
## 해당 값의 개수 count(값) 

## 리스트 거꾸로 순서 배치
r.sort(reverse=True)
>>>[5,4,3,3,2,2,1,1]
## 리벌스 취소
r.reverse()
>>>[1,1,2,2,3,3,4,5]

## 스플릿트 : 특정 문자열을 기준으로 나눠 리스트 생성
s = 'My name is Mike'
to_split = s.split(' ')
print(to_split)

### 스플릿으로 만들어진 리스트를 다시 붙이기  -- 이어붙일 문자 .join(리스트)
x = ' '.join(to_split)
print(x)
>>>'My name is Mike'
```



### 리스트 복사 -- 주의 깊게 봐라 19강의

```python
## 리스트 복사시 수치 전달과 참조 전달이 있다.

## 참조 전달 -주소를 복사(같은 주소를 가리킨다)한 것이기 때문에 j 의 값이 변경되면 i 값도 같이 변경된다 -- 정수 숫자는 수치 전달이다
i = [1,2,3,4,5]
j = i
j[0]=100
j = [100,2,3,4,5]
i = [100,2,3,4,5]
## 수치 전달 - 값만 복사 y 변경시 x에 영향 없음
x =[1,2,3,4,5]
#y = x[:]
y = x.copy()
y[0]=100
x = [1,2,3,4,5]
y = [100,2,3,4,5]
```

![image-20210609173455118](C:\Users\SEONGSOO\AppData\Roaming\Typora\typora-user-images\image-20210609173455118.png)



### Tuple 내가 몰랐던 사실

```python
## 튜플 안의 리스트 값은 변경 가능 (리스트 전체 변경은 불가능?)
t = ([1,2,3,4],[5,6,7])
t[0] =[1] 
>>TypeError

t[0][0] = 100
print(t)
>>>([100,2,3,4],[5,6,7])
```



### 튜플의 언패킹

```python
x , y = 10, 20

## 두 숫자 값 바꾸기
a = 100
b = 200
a,b = b,a
```



### 사전형 

```python
## dict 생성 법 내가 모르는 방법
#1
dict('a'=10,'b'=20)
{'a':10,'b':20}
#2
dict([('a',10),('b',20)])
{'a':10,'b':20}
```



### 사전형 메소드

```python
d ={'x':10,'y':20}

## 키값만 꺼내고 싶을 때 key()
d.keys()
>>>dic_keys(['x','y'])

## 값만 꺼내고 싶을 때 values()
d.values()
>>dict_values([10,20])

d2 = {'x':1000,'j':500}
# 두개의 dict 연산
# update(dict) 같은 키의 값은 d2값으로 , 없는 키가 있으면 추가
d.update(d2)
>>{'x':1000,'y':20,'j':500}

## dict 키를 가지고 값 가져오기 get(key)
d.get('x')
>>>1000

## 값을 꺼내고 삭제 pop(key)
d.pop('x')
>>>1000
print(d)
>>>{'y':20,'j':500}
## del d d라는 객체 삭제
## clear() 모든 값 삭제
d.clear()
print(d)
>>>{}

d = {'a':100,'b':200}
## 해당 키가 dict에 있는지 확인 
'a' in d
>>> True
'j' in d
>>> False
```



### 사전형의 복사

리스트 복사와 똑같다

```python
## 수치 전달 copy를 이용해서 수치 전달
x = {'a':1}
y = x.copy()
y['a'] = 1000
x = {'a':1}
y = {'a':1000}
```





### 집합 형 Set

```python
## 중복되는 값은 제거
a = {1,2,2,3,4,4,4,5,6}
print(a)
>>>{1,2,3,4,5,6}

b = {2,3,3,6,7}

## a에서 b의 값 제거 ( 교집합 제거)
a -b
{1,4,5}

b-a
{7}

##a와 b 둘다 가지고 있는 값 교집합
a & b
{2,3,6}

### 합집합
a | b
{1,2,3,4,5,6,7}

###집합의 대칭 차 ( 서로한테만 있는 값만 )
a ^ b
{1,4,5,7}
```



### 집합형 메소드

```python
s = {1,2,3,4,5}
## set 은 index가 없다  
## 값 추가 add(값)
s.add(6)
>>>{1,2,3,4,5,6}
##값 삭제 remove(6)
s.remove(6)
## 모든 값 삭제 clear()
s.clear()
##사전형과 집합형 구분 방법
s
>>>set()
```



### 집합형 사용 예

```python
## 리스트형을 집합형으로 형 변환
# 주로 중복값 삭제를 위해 사용
f = [1,1,2,2,3,3,3,4,4,5,5]
kind = set(f)
print(kind)
>>>{1,2,3,4,5}
```



### 파이썬 법칙

```python
# 코드 한줄이 길어질 경우 () 아니면 \ 를 이용해라
s = ('aaaaaaaaaaaaaaaaa'
    +'bbbbbbbbbbbbbbbbbb')
b = 'aaaaaaaaaaaaaaaaa'\
    +'bbbbbbbbbbbbbbbbbb'
```



## 제어문

### if 문

``` python
## elif 문은 조건이 같으면 제일 처음 조건으로 들어간다
## elif 문은 처음 if 문의 조건이 만족 되면 들어오지 않는다


## 조건문 not을 쓸 때 (숫자 비교일 때는 쓰지 않는다)
## boolean 값을 부정할 경우에 쓰인다 


## 어떤 변수에 값이 들어 있는지 없는지 판별하는 방법
## 값이 들어있으면 True 
## 값이 비어있으면 False  ex) [], {}, set(), (), 0, 0.0, ''
#is_ok = True
is_ok = 1 #True
is_ok = 0 #False

if is_ok:
    print('OK!')
else:
    print('NO!')

    
## None 판정
is_empty = None
if is_empty is None:  #is_empty == None이라 하지 않는다 주로 is 사용
    print('None!!') 
    
## is는 주로 값 비교에는 사용하지 않고 boolean 과 None 의 비교에 사용된다?
```



 

### While 문 

```python
## while else 문 
#while 문이 끝나면 else 문 실행 (단, while 안에 break 가 없을 경우에만)
count =0
while count < 5
	print(count)
	count +=1
else:
    print('done')
```



### for문

```python
## range(시작할 index 또는 숫자-처음부터면 생략 가능 , 끝자리, 건너뛸 자리수- 없으면 생략 가능)
for i in range(2,10,3):
    print(i)
>>>2
5
8

## index i를 사용하지 않겠다 라면 _ 로 표현
for _ in range(10):
    print('hello')
    
## enumerate 함수 - index까지 함께 표현 하려면

for i,fruit in enumerate(['apple','banana','orange']):
    print(i,fruit)
    
## zip 함수 i 를 여러번 쓰지 않고 여러 리스트를 한번에 순서대로 출력 ( 제일 작은 길이를 가진 list 기준으로 출력)
days = ['Mon','Tue',"Wed"]
fruits = ['apple','banana','orange']
drinks = ['coffee','tea','beer']

for day , fruit, drink in zip(days, fruits, drinks):
    print(day, fruit, drink)

    
## dict 형태를 for 문으로 출력 items()
d = {'x':100, 'y': 200}

for k , v in d.items():
    print(k,':',v)
    
print(d.items())
>>> dict_items([('x',100),('y',200)])
```



### 함수

```python
## 함수 인자와 return 값의 type 정하기
def add_num(a : int , b : int) -> int:
    return a + b
### 하지만 문자열을 인자로 주어도 실행되긴 함

## 인자 전달시 해당 인자명(위치인수)을 같이 적어 주면 실수 할 일이 없다(하지만 반드시 모든인자를 적어주거나 순서에 맞게 적어준다)
def menu(entree='beef', drink='wine', desert='ice'): # defualt 인자가 있으면 모든 인자를 다 적을 필요가 없다
    print(entree)
    print(drink)    
    print(desert)
menu(entree='beef',desert='ice',drink='beer')
menu('beef',desert='ice',drink='beer') #menu(desert='ice','beef',drink='beer') 오류
menu(entree='chicken')

```

