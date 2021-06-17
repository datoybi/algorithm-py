'''
    힙과 배열 
        일반적으로 힙 구현시 배열 자료구조를 활용함
        배열은 인덱스가 0번부터 시작하지만, 힙 구현의 편의를 위해, root 노드 인덱스 번호를 1로 지정하면, 구현이 좀더 수월함
            부모 노드 인덱스 번호(parent node's index) = 자식 노드 인덱스 번호 (child node's index) //2
            왼쪽 자식 노드 인덱스 번호 (left child node's index) = 부모 노드 인덱스 번호 (parent node's index) *2
            오른쪽 자식 노드 인덱스 번호 (right child node's index) = 부모 노드 인덱스 번호 (parent node's index) *2+1

'''
# 힙의 데이터 삽입
#  1. 완전 이진트리처럼 데이터 채우기 2. 부모노드와 비교를 해서 부모노드보다 작을 떄 까지 바꿔주는 작업
class Heap:
    #완전 이진트리처럼 데이터 채우기
    def __init__(self, data):
        self.heap_array = list() 
        self.heap_array.append(None) # 맨 앞 노드는 0으로 노드가 1부터 시작하는게 더 보기 편하기 때문
        self.heap_array.append(data)

    def move_up(self, inserted_idx):  # 루트노드와 비교하여 바꿔야되는지 판단해주는 메서드
        if inserted_idx <=1: # inserted_idx가 root node 일 때
            return False
        parent_idx = inserted_idx // 2
        if self.heap_array[inserted_idx] > self.heap_array[parent_idx]:
            return True
        else:
            return False

    def insert(self, data): # 초기화
        if len(self.heap_array) == 0:
            self.heap_array.append(None)
            self.heap_array.append(data)
            return True
        self.heap_array.append(data)
    #  부모노드와 비교를 해서 부모노드보다 작을 떄 까지 바꿔주는 작업  
        inserted_idx = len(self.heap_array)-1 # 배열[0]번째에 None을 넣었으니 len에서 -1을 해준다

        while self.move_up(inserted_idx):
            parent_idx = inserted_idx//2 # 부모노드 인덱스 번호
            self.heap_array[inserted_idx], self.heap_array[parent_idx] = self.heap_array[parent_idx], self.heap_array[inserted_idx] # swap a,b = b,a
            inserted_idx = parent_idx # 인덱스 번호도 바꿔주기

        return True


heap = Heap(15)
heap.insert(10)
heap.insert(8)
heap.insert(5)
heap.insert(4)
heap.insert(20)
print(heap.heap_array)