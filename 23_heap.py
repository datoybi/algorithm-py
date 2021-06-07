'''
    힙의 데이터 삭제 구현 (Max Heap 예)
        보통 삭제는 최상단 노드(root노드)를 삭제하는 것이 일반적임 
            힙의 용도는 최대값 또는 최소값을 root 노드에 놓아서, 최대값과 최소값을 바로 꺼내 쓸 수 있도록 하는 것임

잘 이해가 안됑 ㅠㅠ


'''

class Heap:
    def __init__(self, data):
        self.heap_array = list()
        self.heap_array.append(None)
        self.heap_array.append(data)

    def pop(self):
        if len(self.heap_array) <= 1:
            return None

        returned_data = self.heap_array[1]
        self.heap_array[1] = self.heap_array[-1]
        del self.heap_array[-1]
        poped_idx = 1

        while self.move_down(poped_idx):
            left_child_popped_idx = popped_idx * 2
            right_child_popped_idx = popped_idx * 2 + 1
            
            # case2: 오른쪽 자식 노드만 없을 때 (왼쪽 있음)
            if right_child_popped_idx >= len(self.heap_array):
                if self.heap_array[popped_idx] < self.heap_array[left_child_popped_idx]:
                    self.heap_array[popped_idx], self.heap_array[left_child_popped_idx] = self.heap_array[left_child_popped_idx], self.heap_array[poped_idx]
                    popped_idx = left_child_popped_idx
            # case3: 왼쪽, 오른쪽 자식 모두 있을 떄
            else:
                if self.heap_array[left_child_popped_idx] > self.heap_array[right_child_popped_idx]:
                    if self.heap_array[poped_idx] < self.heap_array[left_child_popped_idx]:
                        self.heap_array[popped_idx], self.heap_array[left_child_popped_idx] = self.heap_array[left_child_popped_idx], self.heap_array[poped_idx]
                        popped_idx = left_child_popped_idx
                else:
                   if self.heap_array[left_child_popped_idx] < self.heap_array[right_child_popped_idx]:
                        self.heap_array[popped_idx], self.heap_array[left_child_popped_idx] = self.heap_array[left_child_popped_idx], self.heap_array[poped_idx]
                        popped_idx = left_child_popped_idx
        return returned_data


heap = Heap(15)
heap.insert(10)
heap.insert(8)
heap.insert(5)
heap.insert(4)
heap.insert(20)
print(heap.heap_array)

heap.pop()


'''
    힙(Heap) 시간복잡도
        depth (트리의 높이)를 h라고 표기한다면, 
        n개의 노드를 가지는 heap에 데이터 삽입 또는 삭제시, 최악의 경우 root 노드에서 leaf 노드까지 비교해야 하므로 h= log2n에 가까우므로, 시간복잡도는 O(logn)
            참고 : 빅오 표기법에서 logn에서의 log의 밑은 10이 아니라 2입니다
            한번 실행시마다, 50%의 실행할 수도 있는 명령을 제거한다는 의미, 즉 50%의 실행시간을 단축시킬 수 있다는 것을 의미함

'''