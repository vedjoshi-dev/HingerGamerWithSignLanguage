from a1_state import State

class Agent:
    def __init__(self, name="B14"):
        self.name = name
        self.mode = ['minimax', 'alphabeta']
        self.depth = 3
    
    def __str__(self):
        return f"{self.name}, your mode is: {self.mode}"

    def next_move(self, state, mode= 'alphabeta'):
        if mode not in self.mode:
            raise ValueError("Unknown mode:" + mode)
        best_letter, best_value = None, float('-inf')
        for letter, r, c in self.moves(state):
            gain, child= self.play(state, letter, r, c)
            value = gain + self.search (child, self.depth - 1, float('-inf'), float('inf'), False, mode == 'alphabeta')
            if value > best_value:
                best_letter, best_value = letter , value
        return best_letter

    def search(self, state, depth, alpha, beta, maximising, prune):
        moves = self.moves(state)
        if depth == 0 or not moves: 
         return 0 
        best = float ('-inf') if maximising else float ('inf')
        for letter, r,c in moves:
            gain, child = self.play(state, letter, r, c)
            if maximising:
                best = max(best, gain + self.search(child, depth - 1, alpha, beta, False,prune))
                alpha = max(alpha,best)
            else: 
                best = min(best, -gain + self.search(child, depth - 1, alpha, beta, True,prune))
                beta = max(beta,best)
            if prune and alpha >= beta:
                break
            return best

    def moves(self, state):
        return [(chr(ord('A') + r * State.size + c), r, c)
            for r in range(State.size)
            for c in range(State.size)
            if state.grid[r][c] > 0]

    def play (self, state,letter, r ,c):
        child = State(state.grid)
        child.move(letter)
        cost = sum(1 for dr in(-1, 0, 1) for dc in (-1, 0, 1)
               if (dr or dc)
               and 0 <= r + dr < State.size and 0 <= c + dc < State.size
               and state.grid [r + dr][c + dc] > 0)
        bonus = 100 if child.numRegions() > state.numRegions () else 0
        return bonus - cost, child 

def tester():
    agent = Agent()
    print(agent)

    sa = State([[1, 1, 0, 0, 1],
                [1, 1, 0, 0, 0],
                [0, 0, 1, 1, 1],
                [0, 0, 0, 1, 1],
                [0, 0, 0, 0, 1]])
            
    print("State sa:")
    print(sa)

    for mode in agent.mode:
        move = agent.next_move(sa,mode)
        print(mode, "chose:", move)
        assert State(sa.grid).move(move) is True
    line = State([[1, 1, 1, 0,0]] + [[0] * 5 for _ in range(4)])
    print("Hinger test:", agent.next_move(line))
    print("Empty board:", agent.next_move(State(None)))

if __name__ == "__main__":
    tester()



                                        


    


        