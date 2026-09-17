class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        freq = Counter(tasks)
        max_heap = [-cnt for cnt in freq.values()]
        heapq.heapify(max_heap)
        q = deque()
        time = 0

        while max_heap or q:
            time += 1
            if max_heap:
                task = heapq.heappop(max_heap) + 1

                if task != 0:
                    q.append([task, time + n])
            
            if q and q[0][1] == time:
                task, _ = q.popleft()
                heapq.heappush(max_heap, task)
        
        return time

