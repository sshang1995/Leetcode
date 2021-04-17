class Node():
    def __init__(self):
        self.key = 0
        self.value = 0
        self.prev = None
        self.next = None
        
class LRUCache:
    # double linked list
    def _add_node(self, node):
        node.prev = self.head
        node.next = self.head.next
        
        self.head.next.prev = node
        self.head.next = node
        
    def _remove_node(self, node):
        prev = node.prev
        new = node.next
        
        prev.next = new
        new.prev = prev
    
    def _move_to_head(self, node):
        self._remove_node(node)
        self._add_node(node)
    
    def _pop_tail(self):
        lastNode= self.tail.prev
        self._remove_node(lastNode)
        return lastNode
        
    def __init__(self, capacity):
        self.cache = {}
        self.size = capacity
        self.head = Node()
        self.tail = Node()
        
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        node = self.cache.get(key)
        if not node:
            return -1
        self._move_to_head(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key)
        
        if not node:
            node = Node()
            node.key = key
            node.value = value 
            
            self.cache[key] = node
            self._add_node(node)
            if len(self.cache) > self.size:
                tail = self._pop_tail()
                del self.cache[tail.key]
        else:
            node.value = value
            self._move_to_head(node)
            

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)