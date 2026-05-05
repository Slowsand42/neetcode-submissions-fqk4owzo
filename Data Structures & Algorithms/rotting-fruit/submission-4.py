class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visit = set()
        q = deque()
        time = fresh = 0

        def addFruit(r, c, fresh):
            if (r < 0 or c < 0 or
                r >= rows or c >= cols or
                (r, c) in visit or grid[r][c] != 1):
                return fresh
            
            visit.add((r, c))
            q.append((r, c))
            fresh -= 1
            return fresh

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))
                    visit.add((r, c))

        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                
                fresh = addFruit(r + 1, c, fresh)
                fresh = addFruit(r - 1, c, fresh)
                fresh = addFruit(r, c + 1, fresh)
                fresh = addFruit(r, c - 1, fresh)

            time += 1

        if fresh == 0:
            return time
        else:
            return -1