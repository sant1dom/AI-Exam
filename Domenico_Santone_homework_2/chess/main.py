import chess

from Agent import Agent
from BestLAgent import BestLAgent
from heuristics.SimpleHeuristic import SimpleHeuristic
from heuristics.WeightedHeuristic import WeightedHeuristic
from heuristics.AbstractHeuristic import AbstractHeuristic
from heuristics.CheckHeuristic import CheckHeuristic
from heuristics.PredictHeuristic import PredictHeuristic
from typing import List

white_wins = 0
black_wins = 0
draws = 0

def main():
    global white_wins, black_wins, draws
    board = chess.Board()
    # This can be commented out if you don't want to see the board

    # This is parameter for the heuristic
    white_depth = 1
    black_depth = 6

    # This is the heuristic
    white_heuristic = PredictHeuristic()
    black_heuristic = WeightedHeuristic()

    # Here you can instantiate a number of agents to play the game
    agents: List[Agent] = []
    # For example in this chess game we have 2 agents
    agents.append(BestLAgent(white_heuristic, white_depth, k=3))
    agents.append(BestLAgent(black_heuristic, black_depth))
    print(f"{white_heuristic} depth={white_depth} {'k='+str(agents[0].k) if hasattr(agents[0], 'k') else '' } vs {black_heuristic} depth={black_depth} {'k='+str(agents[1].k) if hasattr(agents[1], 'k') else '' }")

    # Generic board game loop
    for _ in range(100):
        while not board.is_game_over():
            for agent in agents:
                if board.is_game_over():
                    break
                move = agent.play(board.copy())
                board.push(move)
                # This is for displaying the game
                # clear_output(wait=True)
                # display(board)
                # time.sleep(0.1)

            # Print the winner
        if board.outcome().winner == chess.WHITE:
            print("White wins")
            white_wins += 1
        elif board.outcome().winner == chess.BLACK:
            print("Black wins")
            black_wins += 1
        else:
            print("Draw")
            draws += 1
        print(white_wins + black_wins + draws, end="\r")
        board.reset()

    print("White wins: " + str(white_wins))
    print("Black wins: " + str(black_wins))
    print("Draws: " + str(draws))
    print("Total: " + str(white_wins + black_wins + draws) + " games")
    print("White win rate: " + str(white_wins / (white_wins + black_wins + draws) * 100) + "%")
    print("Black win rate: " + str(black_wins / (white_wins + black_wins + draws) * 100) + "%")
    print("Draw rate: " + str(draws / (white_wins + black_wins + draws) * 100) + "%")


if __name__ == '__main__':
    main()
