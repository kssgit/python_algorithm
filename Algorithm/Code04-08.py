## 클래스와 함수 선언 부분 ##
class Node() :
	def __init__ (self) :
		self.data = None
		self.link = None

def printNodes(start) :
	current = start
	if current == None :
		return
	print(current.data, end = ' ')
	while current.link != None:
		current = current.link
		print(current.data, end = ' ')
	print()


def insert_node(findData, insertData):
	global memory,head,pre,current

	if head.data == findData: # 첫노드에 찾는 값이 있으면 첫 노드 삽입
		node = Node()
		node.data = insertData
		node.link = head
		head = node
		return
	current = head
	while current.link!=None:  # 중간 노드 앞에 삽입
		pre = current
		current = current.link
		if current.data == findData :
			node = Node()
			node.data = insertData
			node.link = current
			pre.link = node
			return

	node = Node()
	node.data=insertData
	current.link=node

def deleteNode(deleteData):
	global memory,head,pre,current

	if head.data == deleteData :
		current=head
		head=head.link
		del(current)
		return

	current=head
	while(current.link!=None):
		pre = current
		current =current.link
		if current.data == deleteData:
			pre.link = current.link
			del(current)
			return

def findNode(findData):
	global memory,head,pre,current

	if head.data == findData :
		return head

	current = head
	while current.link != None:
		current = current.link
		if current.data == findData:
			return  current
	return Node()






## 전역 변수 선언 부분 ##
memory = []
head, current, pre = None, None, None
# head는 첫 번째 node
# pre 는 이전 노드 
# current는 현재 노드

dataArray = ["다현", "정연", "쯔위", "사나", "지효"]

## 메인 코드 부분 ##
if __name__ == "__main__" :

	node = Node()		# 첫 번째 노드
	node.data = dataArray[0]
	head = node
	memory.append(node)

	for data in dataArray[1:] :	# 두 번째 이후 노드
		pre = node
		node = Node()
		node.data = data
		pre.link = node
		memory.append(node)

	printNodes(head)
	insert_node("다현","화사")
	printNodes(head)
	insert_node('사나','솔라')
	printNodes(head)
	insert_node('재남','문별')
	printNodes(head)


	deleteNode("화사")
	printNodes(head)
	deleteNode("쯔위")
	printNodes(head)
	deleteNode("문별")
	printNodes(head)
	deleteNode("재남")
	printNodes(head)


	print(findNode(input("찾을 데이터를 입력하세요")).data)
