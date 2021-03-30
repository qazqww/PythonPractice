# https://codeup.kr/problem.php?id=4503
# 파이썬의 LinkedList와 Called by sharing을 접함

class Node:
    def __init__(self, data):        
        self.data = data
        self.checked = 0
        self.next = None

    def append(self, data):
        temp = self
        while temp.next != None:
            temp = temp.next
        temp.next = Node(data)

    def get_all_next(self):
        next_list = []
        temp = self
        while temp.next != None:
            next_list.append(temp.next.data)
            temp = temp.next
        return next_list

cpus = []

cpu_num = int(input())
for i in range(cpu_num):
    cpus.append(Node(i))

pair_num = int(input())
for i in range(pair_num):
    no1, no2 = map(int, input().split())
    cpus[no1 - 1].append(no2 - 1)
    cpus[no2 - 1].append(no1 - 1)

queue = [0]
cpus[0].checked = 1

while len(queue) != 0:
    num = queue.pop(0)
    next_list = cpus[num].get_all_next()
    for next in next_list:
        if cpus[next].checked == 0:
            cpus[next].checked = 1
            queue.append(next)    

cnt = -1
for cpu in cpus:
    if cpu.checked == 1:
        cnt += 1
print(cnt)