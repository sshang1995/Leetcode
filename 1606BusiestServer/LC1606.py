class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        busy_jobs = []  # heap (job_end_time, node) to free up the nodes quickly
        after = [] # heap (nodes) free after current server
        before = list(range(k))  # heap (nodes) to use for loopback
        requests_handled = [0] * k

        for i, (arrvl, ld) in enumerate(zip(arrival, load)):
            server_id = i % k
            if server_id == 0:  # loopback
                after = before
                before = []

            while busy_jobs and busy_jobs[0][0] <= arrvl:
                freed_node = heapq.heappop(busy_jobs)[1]
                if freed_node < server_id: heapq.heappush(before, freed_node)
                else: heapq.heappush(after, freed_node)

            use_queue = after if after else before
            if not use_queue: continue  # request dropped
            using_node = heapq.heappop(use_queue)
            requests_handled[using_node] += 1
            heapq.heappush(busy_jobs, (arrvl + ld, using_node))

        maxreqs = max(requests_handled)
        return [i for i, handled in enumerate(requests_handled) if handled == maxreqs]
