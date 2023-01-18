import chess

from Agent import Agent
from heuristics.SimpleHeuristic import SimpleHeuristic
from heuristics.WeightedHeuristic import WeightedHeuristic
from heuristics.AbstractHeuristic import AbstractHeuristic
from heuristics.CheckHeuristic import CheckHeuristic
from typing import List

white_wins = 0
black_wins = 0
draws = 0


def print_winner(board):
    global white_wins
    global black_wins
    global draws
    if board.outcome().winner == chess.WHITE:
        white_wins += 1
        print("White wins")
    elif board.outcome().winner == chess.BLACK:
        black_wins += 1
        print("Black wins")
    else:
        draws += 1
        print("Draw")
    print(white_wins + black_wins + draws, end="\r")


def main():
    board = chess.Board()
    # This can be commented out if you don't want to see the board

    # This is parameter for the heuristic
    white_depth = 2
    black_depth = 2

    # This is the heuristic
    white_heuristic = WeightedHeuristic()
    black_heuristic = CheckHeuristic()

    print(f"{white_heuristic} vs {black_heuristic}")
    print(1, end="\r")
    # Here you can instantiate a number of agents to play the game
    agents: List[Agent] = []
    # For example in this chess game we have 2 agents
    agents.append(Agent(white_heuristic, white_depth))
    agents.append(Agent(black_heuristic, black_depth))
    # Generic board game loop
    for _ in range(50):
        while not board.is_game_over():
            for agent in agents:
                if board.is_game_over():
                    break
                move = agent.play(board)
                board.push(move)
                # This is for displaying the game
                # clear_output(wait=True)
                # display(board)
                # time.sleep(0.1)

        # Print the winner
        if board.outcome().winner == chess.WHITE:
            print("White wins")
        elif board.outcome().winner == chess.BLACK:
            print("Black wins")
        else:
            print("Draw")
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
