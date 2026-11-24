from a1_state import State
from a2_agent import Agent

def play(state, agentA, agentB):
    scoreA = 100
    scoreB = 100

    if agentA is None:
        nameA = "Human A"
    else:
        nameA = agentA.name

    if agentB is None:
        nameB = "Human B"
    else:
        nameB = agentB.name

    currentPlayer = 0

    while any(1 in row for row in state.grid):

      if currentPlayer == 0:
          player = agentA
          playerName = nameA
      else:
          player = agentB
          playerName = nameB

      print(playerName, "s turn")

      if player is None:
        move = input("Enter your move (A-Y or Z): ")
      else:
        move = player.next_move(state)

      if move == "Z":
            print(playerName, "played Z and loses!")
            return playerName, "lost"

def tester():
    pass

if __name__ == "__main__":
    tester()