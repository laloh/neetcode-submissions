class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        freq = Counter(tasks)
        heap = [-cnt for cnt in freq.values()]
        heapq.heapify(heap)
        time = 0
        queue = deque()

        while queue or heap:
            time += 1
    
            if heap:
                task = heapq.heappop(heap) + 1
                
                if task != 0:
                    queue.append([task, time + n])
                
            if queue and queue[0][1] == time:
                task, _ = queue.popleft()
                heapq.heappush(heap, task)
        
        return time


