'''
    힙의 데이터 삭제 구현 (Max Heap 예)
        보통 삭제는 최상단 노드(root노드)를 삭제하는 것이 일반적임 
            힙의 용도는 최대값 또는 최소값을 root 노드에 놓아서, 최대값과 최소값을 바로 꺼내 쓸 수 있도록 하는 것임
        
        데이터 삭제 방법
            가장 최하단부 왼쪽에 위치한 노드(가장 나중에 추가한 노드)를 root로 이동
            root노드의 값이 child node보다 작을 경우, root 노드의 child node 중 가장 큰 값을 가진 노드와 root 노드를 바꿔주는 작업을 반복함(swap)
            
            좀 이해되긴 하는데 완벽히는 아님 ㅠ
'''

class Heap:
    def __init__(self, data):
        self.heap_array = list()
        self.heap_array.append(None)
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
        
    ######################################### 삭제 #########################################

    def move_down(self, popped_idx):
        left_child_popped_idx = popped_idx * 2
        right_child_popped_idx = popped_idx * 2 + 1
        
        # case1: 왼쪽 자식 노드도 없을 때
        if left_child_popped_idx >= len(self.heap_array): # ?
            return False
        # case2: 오른쪽 자식 노드만 없을 때
        elif right_child_popped_idx >= len(self.heap_array): # ?
            if self.heap_array[popped_idx] < self.heap_array[left_child_popped_idx]: # popped_idx보다 왼쪽이 더 클때
                return True
            else:
                return False
        # case3: 왼쪽, 오른쪽 자식 노드 모두 있을 때
        else:
            if self.heap_array[left_child_popped_idx] > self.heap_array[right_child_popped_idx]: # 오른쪽보다 왼쪽이 더 클때
                if self.heap_array[popped_idx] < self.heap_array[left_child_popped_idx]: # popped_idx보다 왼쪽이 더 클때
                    return True
                else:
                    return False
            else: # 왼쪽보다 오른쪽이 더 클때
                if self.heap_array[popped_idx] < self.heap_array[right_child_popped_idx]:  # popped_idx보다 오른쪽이 더 클때
                    return True
                else:
                    return False
    
    def pop(self):
        if len(self.heap_array) <= 1: # heap_array가 없는 경우
            return None
        
        returned_data = self.heap_array[1] # root node
        self.heap_array[1] = self.heap_array[-1] # 루트 노드와 마지막에 삽입된 노드 교환
        del self.heap_array[-1] # 루트 노드 삭제
        poped_idx = 1 # 현재 노드는 인덱스 1(루트)에 있음

        # 자식 노드가 없거나 자식 노드가 더 클때 까지 반복
        while self.move_down(popped_idx):
            left_child_popped_idx = popped_idx * 2
            right_child_popped_idx = popped_idx * 2 + 1

            # case2: 오른쪽 자식 노드만 없을 때
            if right_child_popped_idx >= len(self.heap_array):
                if self.heap_array[popped_idx] < self.heap_array[left_child_popped_idx]:
                    self.heap_array[popped_idx], self.heap_array[left_child_popped_idx] = self.heap_array[left_child_popped_idx], self.heap_array[popped_idx]
                    popped_idx = left_child_popped_idx
            # case3: 왼쪽, 오른쪽 자식 노드 모두 있을 때
            else:
                if self.heap_array[left_child_popped_idx] > self.heap_array[right_child_popped_idx]:
                    if self.heap_array[popped_idx] < self.heap_array[left_child_popped_idx]:
                        self.heap_array[popped_idx], self.heap_array[left_child_popped_idx] = self.heap_array[left_child_popped_idx], self.heap_array[popped_idx]
                        popped_idx = left_child_popped_idx
                else:
                    if self.heap_array[popped_idx] < self.heap_array[right_child_popped_idx]:
                        self.heap_array[popped_idx], self.heap_array[right_child_popped_idx] = self.heap_array[right_child_popped_idx], self.heap_array[popped_idx]
                        popped_idx = right_child_popped_idx
        
        return returned_data
    

heap = Heap(15)
heap.insert(10)
heap.insert(8)
heap.insert(5)
heap.insert(4)
heap.insert(20)
print(heap.heap_array)

heap.pop()
print(heap.heap_array)


'''
    힙(Heap) 시간복잡도
        depth (트리의 높이)를 h라고 표기한다면, 
        n개의 노드를 가지는 heap에 데이터 삽입 또는 삭제시, 최악의 경우 root 노드에서 leaf 노드까지 비교해야 하므로 h= log2n에 가까우므로, 시간복잡도는 O(logn)
            참고 : 빅오 표기법에서 logn에서의 log의 밑은 10이 아니라 2입니다
            한번 실행시마다, 50%의 실행할 수도 있는 명령을 제거한다는 의미, 즉 50%의 실행시간을 단축시킬 수 있다는 것을 의미함

'''