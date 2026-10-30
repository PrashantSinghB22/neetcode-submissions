class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}  # Map key to node

        # left = LRU, right = MRU
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left

    # Remove a node from the list
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    # Insert a node at the right (MRU) end
    def insert(self, node):
        prev, nxt = self.right.prev, self.right

        prev.next = node
        nxt.prev = node

        node.prev = prev
        node.next = nxt

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]

            self.remove(node)
            self.insert(node)

            return node.val

        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])

        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            # Remove the LRU node
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
