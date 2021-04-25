# Data structure & Algorithm 



## 리스트 / 선형 자료 구조



### 선형 리스트 



### 단순 연결 리스트 

물리적으로 떨어진 곳에 위치 

각 노드별 링크로 연결

 

**노드의 구조** 

데이터 , 링크



**용어**

head 

가장 첫번 째 노드



메모리

모든 노드가 담아진 공간



pre, current

pre 이전 노드

current 현재 노드



**노드의 생성** 

```python
class Node() :
	def __init__ (self) :
		self.data = None
		self.link = None
```

**노드 연결**

```python
node1 = Node()
node1.data = "다현"

node2 = Node()
node2.data = "정연"
node1.link = node2
```



**삽입** 

첫번 째 삽입 



중간에 삽입



마지막에 삽입



**삭제**

첫번 째 노드 삭제



중간 노드 삭제



마지막 노드 삭제



**검색**




### 원형 연결 리스트 

단순 연결 리스트에서 마지막 노드의 링크가 head를 가리킨다 



### 스택 

먼저 들어간 데이터가 가장 나중에 나온다 

스택의 자료구조는 한쪽 끝이 막힌 형태(입구가 하나)

가장 나중에 써야할 데이터를 가장 먼저 넣는다



용어

top :가장 위의 데이터 자리

push : 데이터를 삽입하는 작동 

pop :데이터를 꺼내는(추출) 작동( 어떤 데이터를 정해서 꺼내지 못하고 top이 가리키는 데이터를 추출)  -> 먼저 데이터를 추출하고 top을 낮춘다 

peek : 맨위의 값 




### 큐

입구와 출구가 있다 

먼저 들어간 데이터를 먼저 찾는다 (first in,first out )



용어

enQueue 큐에 데이터 삽입하는 작동 (rear를 증가시키고 데이터 삽입)

deQueue 데이터를 추출하는 작동(front를 증가시키고 데이터 추출)

front 맨처음 자리

rear 마지막 자리





## 비 선형 자료 구조



## 이진 트리

