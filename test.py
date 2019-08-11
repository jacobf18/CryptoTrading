import queue

l = queue.Queue()

l.put(1)
l.put(2)
print(l.get())
print(l.get())
print(l.full())
