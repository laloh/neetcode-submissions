class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        """
         {
            X: 2
            Y: 2
         }

         - Most frequent tasks go firsts (max_heap)
         - We need queue to enqueue the process when is being used
         - We need a timer to check if most used task is ready to be in heap
         -  
        """

        frequency = Counter(tasks)
        max_heap = [-cnt for cnt in frequency.values()]        
        heapq.heapify(max_heap) # put the most frequent at the beginning

        time = 0
        q = deque()

        while max_heap or q:
            time += 1
            if max_heap:
                interval = heapq.heappop(max_heap) + 1
                if interval != 0:
                    q.append([interval, time+n])

            if q and q[0][1] == time:
                interval, time = q.popleft()
                heapq.heappush(max_heap, interval)
        
        return time
