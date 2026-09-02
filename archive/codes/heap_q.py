# In Python, heaps are used to implement priority queues, where the smallest (or largest)
# element is always accessible efficiently. Python provides the heapq module for heap operations.
# - Key Heap Operations
# - heapq.heapify(list) → Converts a list into a heap.
# - heapq.heappush(heap, item) → Adds an element while maintaining heap order.
# - heapq.heappop(heap) → Removes and returns the smallest element.
# - heapq.heappushpop(heap, item) → Pushes an item and pops the smallest in one step.
# - heapq.heapreplace(heap, item) → Pops the smallest and pushes a new item.
#   Example: Min-Heap in Python


import heapq

# Create a heap
heap = [10, 20, 15, 30, 40]
heapq.heapify(heap)  # Convert list into a heap

# Push an element
heapq.heappush(heap, 5)

# Pop the smallest element
min_element = heapq.heappop(heap)

print("Heap:", heap)
print("Smallest element:", min_element)
