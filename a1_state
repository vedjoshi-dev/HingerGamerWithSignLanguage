#(Groupnumberidk?, 100464097, everyone elses id)

class State:
    size = 5
    def __init__(self, grid):
        if grid is None:
            self.grid = [[0 for _ in range(State.size)] for _ in range(State.size)]
        else:
            assert(len(grid) == State.size)
            assert all(len(row) == State.size for row in grid)
            self.grid = [row[:] for row in grid]

    def __str__(self):
        out = ''
        for row in self.grid:
            out += ' '.join(str(cell) for cell in row) + '\n'
        return out

    def move(self, letter):
        position = ord(letter) - ord('A')

        row = position // State.size
        col = position % State.size

        if self.grid[row][col] == 1:
            self.grid[row][col] = 0
            return True

        return False
    
    def successors(self):
        for r in range(State.size):
            for c in range(State.size):
                if self.grid[r][c] > 0:
                    new_state  = State(self.grid)
                    new_state.grid[r][c] = self.grid[r][c] - 1
                    yield new_state      


    def adjacentOnes(self,r,c,markedOnes):

        #Values to be added to (r,c) to find adjacent cells
        adjacency = [
            (-1, -1),  # up-left
            (-1, 0),   # up
            (-1, 1),   # up-right
            (0, -1),   # left
            (0, 1),    # right
            (1, -1),   # down-left
            (1, 0),    # down
            (1, 1)     # down-right
        ]
        
        #Check each adjacent cell to see if it contains a one and is not in markedOnes
        for ar, ac in adjacency:
            if 0 <= r + ar < State.size and 0 <= c + ac < State.size:
                if self.grid[r+ar][c+ac] == 1 and not (r+ar,c+ac) in markedOnes:
                    markedOnes.append((r+ar,c+ac))
                    self.adjacentOnes(r+ar,c+ac,markedOnes)


    def numRegions(self):
        numRegions = 0

        #list containing cells which contain a counter
        markedOnes = []

        #if cell contains a 1 and isn't stored in markedOnes, add to markedOnes and find all cells in that active region
        for r in range(State.size):
            for c in range(State.size):
                        if self.grid[r][c] == 1 and (r,c) not in markedOnes:
                            markedOnes.append ((r,c))
                            numRegions = numRegions + 1
                            self.adjacentOnes(r,c,markedOnes)
        return numRegions

    def numHingers(self):
        numHingers = 0
        currentRegions = self.numRegions()
        stateList = list(self.successors())

        #iterate through reachable states and identify how many contain more active regions than current state
        for s in stateList:
            if s.numRegions() > currentRegions:
                numHingers= numHingers + 1
        return numHingers


    def tester():
        empty = [[0] * 5 for _ in range(5)]
        sa = State([[1, 1, 0, 0, 1],
                    [1, 1, 0, 0, 0],
                    [0, 0, 1, 1, 1],
                    [0, 0, 0, 1, 1],
                    [0, 0, 0, 0, 1]])
        
        print("State sa:")
        print(sa)

        s = State(sa.grid)
        print("move ('Y'):", s.move('Y'))
        print (s)

        print("move ('Y') again:", s.move('Y'))
    
        print ("Unchanged:", sa.grid[4][4] == 1)

        succs = list(sa.successors())
        print("Number of successors:", len(succs))
        print ("First Successor:")
        print(succs[0])

        print ("NumRegion = ", s.numRegions())
        print("numHingers= ", s.numHingers())

if __name__ == "__main__":
    State.tester()
 