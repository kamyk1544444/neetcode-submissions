class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
    
        count = Counter(tasks)

        symbols = [-c for c in count.values()]

        heapq.heapify(symbols)

        time = 0

        q = deque()

        while symbols or q:
            
            time +=1

            if not symbols:
                time = q[0][1]
            else:
                temp = 1 + heapq.heappop(symbols)

                if temp != 0:
                    q.append([temp,time+n])

            if q and q[0][1] == time:
                heapq.heappush(symbols,q.popleft()[0])
        
        return time
        