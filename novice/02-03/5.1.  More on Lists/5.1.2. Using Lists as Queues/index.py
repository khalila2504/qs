from collections import deque
queue = deque(["aya", "khalila", "fathiya"])
queue.append("ayes")
queue.append("ayak")
print(queue.popleft())
print(queue.popleft())
print(queue)