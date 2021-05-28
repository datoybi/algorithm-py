# 08. 큐
'''
    시뮬 가능한 사이트
    https://visualgo.net/en/list

  가장 먼저 넣은 데이터를 가장 먼저 꺼낼 수 있는 구조(호스)
    FIFO(First In First Out), LILO(Last In Last Out)
    Enqueue: 큐에 데이터를 넣는 기능
    Dequeue: 큐에 데이터를 꺼내는 기능

  어디에 큐가 많이 쓰일까?
    멀티 테스킹을 위한 프로세스 스케쥴링 방식을 구현하기 위해 많이 사용됨 (운영체제 참조), 스케쥴링 방식을 함께 이해해두는 것이 좋음

import queue

data_queue = queue.Queue()
data_queue.put("funcoding")
data_queue.put("helloWorld")
data_queue.put(1)

print(data_queue.qsize()) # 3
print(data_queue.get()) # funcoding
print(data_queue.qsize()) # 2
print(data_queue.get()) # helloWorld
print(data_queue.qsize()) # 1



# LifoQueue()
import queue;
data_queue = queue.LifoQueue()
data_queue.put("funcoding")
data_queue.put(2)

print(data_queue.qsize()) # 2
print(data_queue.get()) # 2


#PriorityQueue()
import queue;
data_queue = queue.PriorityQueue()
data_queue.put((10, "Korea")) #priority, value
data_queue.put((5, 1))
data_queue.put((15, "China"))
print(data_queue.qsize()) # 3
print(data_queue.get()) # (5, 1)
print(data_queue.get()) # (10, 'Korea')

'''
queue_list = list()

def enqueue(data) :
    queue_list.append(data)

def dequeue() :
    data = queue_list[0]
    del queue_list[0]
    return data
    
for index in range(10): # 0~9
    enqueue(index)

print(len(queue_list))
print(dequeue())
print(dequeue())