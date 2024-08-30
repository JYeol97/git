# 파이썬에서는 heapq 라이브러리를 통해서
# heapify 한 상태로 유지가 되는 리스트(배열)를 만들 수 있음
from heapq import heapify, heappop, heappush

class Heap():
    def __init__(self, key=lambda x: x):  # key : 어떤 순서로 입력을 받을거냐
        self.hq = []
        self.key = key

    def push(self, x):  # push 할때 해당되는 x요소
        heappush(self.hq, (self.key(x), x))  # 우리가 원하는 건 두번째 요소 튜플로 넣음 (알아서 정렬이 되도록)

    def pop(self):
        return heappop(self.hq)[1]  # 우리가 원하는 건 두번째 요소라 [1]붙임

    def __len__(self):
        return len(self.hq)


# 최소 힙
mnheap = Heap()

mnheap.push(5)  # 삽입하고 싶다면 아무 숫자나 넣음
mnheap.push(1)
mnheap.push(6)
mnheap.push(8)
mnheap.push(2)
mnheap.push(0)
print(mnheap.hq)
x = mnheap.pop()
print(x)
x = mnheap.pop()
print(x)
x = mnheap.pop()
print(x)
x = mnheap.pop()
print(x)
x = mnheap.pop()
print(x)
x = mnheap.pop()
print(x)

print("----------------------------------------")
# 최대 힙
mxheap = Heap(lambda x: -x)
mxheap.push(5)  # 삽입하고 싶다면 아무 숫자나 넣음
mxheap.push(1)
mxheap.push(6)
mxheap.push(8)
mxheap.push(2)
mxheap.push(0)
print(mxheap.hq)
y = mxheap.pop()
print(y)
y = mxheap.pop()
print(y)
y = mxheap.pop()
print(y)
y = mxheap.pop()
print(y)
y = mxheap.pop()
print(y)
y = mxheap.pop()
print(y)

from functools import cmp_to_key


# 비교 함수
def compare(posA, posB):
    if posA[0] == posB[0]:
        return posB[1] < posA[1]
    return x[0] < y[0]


heap = Heap(key=cmp_to_key(compare))
