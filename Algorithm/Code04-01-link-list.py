class Node() :
	def __init__ (self) :
		self.data = None
		self.link = None

node1 = Node()
node1.data = "다현"

node2 = Node()
node2.data = "정연"
node1.link = node2

node3 = Node()
node3.data = "쯔위"
node2.link = node3

node4 = Node()
node4.data = "사나"
node3.link = node4

node5 = Node()
node5.data = "지효"
node4.link = node5

print(node1.data, end = ' ') #node1 데이터
print(node1.link.data, end = ' ') # node1이 가리키고 있는 node2의 데이터
print(node1.link.link.data, end = ' ') #node2가 가리키고 있는 node3의 데이터
print(node1.link.link.link.data, end = ' ')
print(node1.link.link.link.link.data, end = ' ')
