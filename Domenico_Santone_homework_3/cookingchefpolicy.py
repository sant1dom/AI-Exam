import random

import numpy as np


class Chef:
    def __init__(self, position: int, beater: bool):
        self.position = position
        self.beater = beater


# The reward function for the agent
def step(state, action, moves_not_allowed, chef, gates, pan, beater_1, beater_2, oven, recipe):
    done = False
    reward = -1
    if action == 'up' and (state, state - 8) not in moves_not_allowed:
        state -= 8
    elif action == 'down' and (state, state + 8) not in moves_not_allowed:
        state += 8
    elif action == 'left' and (state, state - 1) not in moves_not_allowed:
        state -= 1
    elif action == 'right' and (state, state + 1) not in moves_not_allowed:
        state += 1
    elif action == 'take' and (state == beater_1 or state == beater_2) and not chef.beater:
        chef.beater = True
        reward = 200
    elif action == 'goright' and state == gates[0]:
        state += 1
    elif action == 'goleft' and state == gates[1]:
        state -= 1
    elif (state == oven and chef.beater and recipe == 'pudding') or (
            state == pan and chef.beater and recipe == 'scrambled'):
        reward = 100
        done = True
    else:
        reward = -100
    return state, reward, done


# Just a utility function to print the two optimal policies
def printpolicy(i):
    if i == 'up':
        print('↑', end=' ')
    elif i == 'down':
        print('↓', end=' ')
    elif i == 'left':
        print('←', end=' ')
    elif i == 'right':
        print('→', end=' ')
    elif i == 'take':
        print('T', end=' ')
    elif i == 'goright':
        print('R', end=' ')
    elif i == 'goleft':
        print('L', end=' ')


def main():
    # The moves that are not allowed (walls)
    moves_not_allowed = [(1, -7), (1, 9), (1, 0),
                         (2, -6),
                         (3, -5),
                         (4, -4), (4, 5),
                         (5, -3), (5, 4),
                         (6, -2),
                         (7, -1), (7, 15),
                         (8, 0), (8, 16), (8, 9),
                         (9, 1), (9, 8), (9, 10),
                         (10, 9), (10, 18),
                         (11, 19),
                         (12, 13),
                         (13, 12),
                         (14, 15),
                         (15, 14), (15, 7),
                         (16, 8), (16, 17),
                         (17, 16), (17, 25),
                         (18, 10), (18, 26),
                         (19, 11),
                         (20, 21),
                         (21, 20),
                         (22, 23),
                         (23, 22), (23, 31),
                         (24, 25),
                         (25, 24), (25, 17), (25, 33),
                         (26, 18), (26, 34),
                         (27, 35),
                         (28, 36), (28, 29),
                         (29, 37), (29, 28),
                         (30, 38),
                         (31, 39), (31, 23),
                         (32, 40), (32, 33),
                         ]
    # The parameters of the environment
    gates = [28, 29]
    pan = 1
    beater_1 = 9
    beater_2 = 15
    oven = 7
    recipe = 'scrambled'
    # recipe = 'pudding'
    chef = Chef(12, False)
    # Q-learning tables, one for the agent before the beater is found and one for the agent after the beater is found
    q_beater = np.zeros((32, 7))
    q_cook = np.zeros((32, 7))
    # The alpha parameter is the learning rate and represents the weight of the new information
    alpha = 0.1
    # The gamma parameter is the discount factor and regulates the importance of future rewards
    gamma = 0.9
    # The set of actions like the ones wrote in the report
    actions = ['up', 'down', 'left', 'right', 'take', 'goright', 'goleft']
    for i in range(10000):
        # The epsilon parameter is the exploration rate and regulates the probability of choosing a random action
        # The decay function is the one showed in the slides
        epsilon = 1 / (i + 1)
        # I reset the state of the agent and the beater every episode
        chef.position = random.randint(1, 32)
        chef.beater = False
        state = chef.position
        done = False
        while not done:
            # Choose an action according to the epsilon-greedy policy
            if np.random.uniform(0, 1) < epsilon:
                action = np.random.choice(actions)
            else:
                # Check if the beater is found and update the Q-table accordingly
                if not chef.beater:
                    action = actions[np.argmax(q_beater[state - 1])]
                else:
                    action = actions[np.argmax(q_cook[state - 1])]

            # Update the state and the reward according to the action always checking if the beater is found
            if not chef.beater:
                next_state, reward, done = step(state, action, moves_not_allowed, chef, gates, pan, beater_1,
                                                beater_2, oven, recipe)
                q_beater[state - 1][actions.index(action)] += alpha * (
                        reward + gamma * np.max(q_beater[next_state - 1]) - q_beater[state - 1][actions.index(action)])
            else:
                next_state, reward, done = step(state, action, moves_not_allowed, chef, gates, pan, beater_1, beater_2,
                                                oven, recipe)
                q_cook[state - 1][actions.index(action)] += alpha * (
                        reward + gamma * np.max(q_cook[next_state - 1]) - q_cook[state - 1][actions.index(action)])
            state = next_state
            chef.position = state

    # Compute the optimal policy
    # The first one is for the agent before the beater is found
    # I used the np.argmax function to find the action with the highest value in the q-table
    beater_policy = np.argmax(q_beater, axis=1)
    beater_policy = [actions[i] for i in beater_policy]

    # The second one is for the agent after the beater is found
    cook_policy = np.argmax(q_cook, axis=1)
    cook_policy = [actions[i] for i in cook_policy]

    # Print the optimal policy (the characters are not ASCII, so they are not displayed correctly in some consoles)
    # You can change them with just 'i' to see the optimal policy if they aren't displayed correctly
    print("Beater policy:")
    for index, i in enumerate(beater_policy):
        printpolicy(i)
        if (index + 1) % 8 == 0:
            print()

    # The character 'X' is the oven or the pan based on the recipe
    print("Cooking policy:")
    for index, i in enumerate(cook_policy):
        if (index == oven - 1 and recipe == 'pudding') or (index == pan - 1 and recipe == 'scrambled'):
            print('X', end=' ')
            continue
        printpolicy(i)
        if (index + 1) % 8 == 0:
            print()


if __name__ == '__main__':
    main()
