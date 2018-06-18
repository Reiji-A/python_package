import collections
import queue

# Double-end queue
collections.deque

q = queue.Queue()
lq = queue.LifoQueue() # [0,1,2]
l = []
d = collections.deque()

for i in range(3):
    q.put(i)
    lq.put(i)
    l.append(i)
    d.append(i)
    print(q,lq,l,d)

#for _ in range(3):
#    print("FIFO queue = {}".format(q.get()))
#    print("LIFO queue = {}".format(lq.get()))
#    print("list       = {}".format(l.pop(0)))
#    print("deque      = {}".format(d.popleft()))

print(d)
d.extendleft("x")
d.extend('y')
print(d)
d.clear()
print(d)
#print(d[1])
#print(d[-1])
#d.rotate()
#print(d)
