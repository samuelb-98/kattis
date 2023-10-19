import sys
import heapq

lower_heap = []
upper_heap = []


for line in sys.stdin:
    if line.strip() == "#":
        median = upper_heap[0]
        heapq.heappop(upper_heap)
        if len(lower_heap) != len(upper_heap):
            heapq.heappush(upper_heap,-lower_heap[0])
            heapq.heappop(lower_heap)
        print(median)
    else:
        line = int(line)
        if upper_heap == [] or line > upper_heap[0]:
            heapq.heappush(upper_heap,line)
            if len(upper_heap) > len(lower_heap) + 1:
                heapq.heappush(lower_heap,-upper_heap[0])
                heapq.heappop(upper_heap)
        else:
            heapq.heappush(lower_heap,-line)
            if len(lower_heap) > len(upper_heap):
                heapq.heappush(upper_heap,-lower_heap[0])
                heapq.heappop(lower_heap)

