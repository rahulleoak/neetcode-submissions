class Solution:
    def isValid(self, row, col, rooms):
        if (
            0 <= row < self.ROWS and
            0 <= col < self.COLS and 
            (row,col) not in self.visited and
            rooms[row][col] == self.room
            ):
            return True
        return False
    
    def islandsAndTreasure(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        self.ROWS, self.COLS = len(rooms), len(rooms[0])
        self.visited = set()
        self.wall, self.gate, self.room = -1, 0, 2147483647
        self.directions = [
            (0,1), (0,-1), (1,0), (-1,0)
        ]
        q = deque()

        for r in range(self.ROWS):
            for c in range(self.COLS):
                if rooms[r][c] == self.gate:
                    self.visited.add((r,c))
                    q.append((r,c))

        distance = 1
        while q:
            levelLen = len(q)
            for _ in range(levelLen):
                room = q.popleft()
                row, col = room

                for dr, dc in self.directions:
                    nr, nc = row + dr, col + dc
                    if self.isValid(nr,nc,rooms):
                        self.visited.add((nr,nc))
                        q.append((nr,nc))
                        rooms[nr][nc] = distance
            distance += 1

